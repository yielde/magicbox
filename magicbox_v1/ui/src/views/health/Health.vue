<!--
 * @Author: Galen Tong
 * @Date: 2022-08-04 22:16:32
 * @LastEditTime: 2022-08-07 21:52:10
 * @Description: 
-->
<template>
	<div>
		<el-card class="box-card">
			<el-form
				:inline="true"
				class="demo-form-inline"
				size="small"
				:model="searchForm"
				ref="searchForm"
			>
				<el-form-item label="信息筛选" prop="title">
					<el-input
						placeholder="信息筛选"
						v-model="searchForm.title"
					></el-input>
				</el-form-item>

				<el-form-item label="时间筛选" prop="dateValue">
					<el-date-picker
						v-model="searchForm.dateValue"
						type="datetimerange"
						start-placeholder="开始日期"
						end-placeholder="结束日期"
						:default-time="['12:00:00']"
					>
					</el-date-picker>
				</el-form-item>

				<el-button size="small" type="primary" @click="clickSearch"
					>筛选</el-button
				>
				<el-button size="small" @click="resetSearchForm('searchForm')"
					>重置</el-button
				>
			</el-form>
		</el-card>

		<el-card class="box-card" style="margin-top: 5px">
			<el-row>
				<el-col :span="24">
					<el-table
						size="mini"
						:data="healthData"
						border
						style="width: 100%"
						highlight-current-row
						:default-sort="{
							prop: 'healthTime',
							order: 'descending',
						}"
					>
						<el-table-column type="index" label="序号">
						</el-table-column>
						<el-table-column
							prop="healthTime"
							label="时间"
							sortable
						>
							<template slot-scope="scope">
								<span v-if="scope.row.isEdit">
									<el-date-picker
										v-model="currentData['healthTime']"
										type="datetime"
										placeholder="选择日期时间"
										align="right"
										:picker-options="pickerOptions"
									>
									</el-date-picker>
								</span>
								<span v-else>
									{{
										scope.row.healthTime
											.replace("T", " ")
											.replace("Z", "")
									}}
								</span>
							</template>
						</el-table-column>

						<el-table-column
							prop="detail"
							label="详细信息"
							sortable
						>
							<template slot-scope="scope">
								<span v-if="scope.row.isEdit">
									<el-input
										v-model="currentData['detail']"
										placeholder="输入内容"
									>
									</el-input>
								</span>
								<span v-else>
									{{ scope.row.detail }}
								</span>
							</template>
						</el-table-column>

						<el-table-column
							prop="text"
							label="标签"
							:filters="selectItem"
							:filter-method="filterTag"
						>
							<template slot-scope="scope">
								<span v-if="scope.row.isEdit">
									<el-select
										v-model="currentData['text']"
										placeholder="疼痛程度"
									>
										<el-option
											v-for="item in selectItem"
											:key="item.value"
											:label="item.text"
											:value="item.value"
										>
										</el-option>
									</el-select>
								</span>
								<span v-else>
									<el-tag
										v-if="scope.row.text === 0"
										type="success"
										>{{ showTag(scope.row.text) }}</el-tag
									>
									<el-tag
										v-else-if="scope.row.text === 1"
										type="warning"
										>{{ showTag(scope.row.text) }}</el-tag
									>
									<el-tag
										v-else-if="scope.row.text === 2"
										type="danger"
										>{{ showTag(scope.row.text) }}</el-tag
									>
								</span>
							</template>
						</el-table-column>

						<el-table-column label="操作">
							<template slot-scope="scope">
								<span
									class="el-tag el-tag--info el-tag--dark"
									style="cursor: pointer; margin-left: 15px"
									@click="
										infoChange(
											scope.row,
											scope.$index,
											true
										)
									"
								>
									{{ scope.row.isEdit ? "保存" : "修改" }}
								</span>
								<span
									v-if="!scope.row.isEdit"
									class="el-tag el-tag--danger"
									style="cursor: pointer; margin-left: 15px"
									@click="deletInfo(scope.row)"
								>
									删除
								</span>
								<span
									v-else
									class="el-tag el-tag--warning"
									style="cursor: pointer; margin-left: 15px"
									@click="
										infoChange(
											scope.row,
											scope.$index,
											false
										)
									"
								>
									取消
								</span>
							</template>
						</el-table-column>
					</el-table>
				</el-col>
				<el-col :span="24">
					<el-button
						type="primary"
						style="width: 100%; margin-top: 24px"
						@click="addHealthInfo()"
					>
						<span>+ 添加</span>
					</el-button>
				</el-col>
			</el-row>
		</el-card>
	</div>
</template>

<script>
	var healthdata = [
		{
			id: 1,
			healthTime: "2022-1-1",
			detail: "疼得不厉害",
			text: 0,
		},
		{
			id: 2,
			healthTime: "2022-2-1",
			detail: "疼得厉害",
			text: 1,
		},
		{
			id: 3,
			healthTime: "2022-3-1",
			detail: "不疼",
			text: 2,
		},
	];
	// var healthdata = []
	export default {
		name: "Health",

		data() {
			return {
				searchForm: {
					title: "",
					category: "",
					dateValue: "",
				},
				selectItem: [
					{ text: "微痛", value: 0 },
					{ text: "中痛", value: 1 },
					{ text: "重痛", value: 2 },
				],
				healthColumns: [
					{ prop: "healthTime", label: "时间" },
					{ prop: "detail", label: "详细信息" },
					{ prop: "text", label: "标签" },
				],
				healthData: [],
				currentData: null,

				pickerOptions: {
					shortcuts: [
						{
							text: "今天",
							onClick(picker) {
								picker.$emit("pick", new Date());
							},
						},
						{
							text: "昨天",
							onClick(picker) {
								const date = new Date();
								date.setTime(date.getTime() - 3600 * 1000 * 24);
								picker.$emit("pick", date);
							},
						},
						{
							text: "一周前",
							onClick(picker) {
								const date = new Date();
								date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
								picker.$emit("pick", date);
							},
						},
					],
				},
			};
		},
		methods: {
			init() {
				healthdata.forEach((row) => {
					row.isEdit = false;
				});
				this.healthData = healthdata;
			},
			filterTag(value, row) {
				return row.text === value;
			},
			clickSearch() {
				console.log(this.searchForm);
			},
			resetSearchForm(formName) {
				this.$refs[formName].resetFields();
			},
			//读取表格数据

			//添加账号
			addHealthInfo() {
				for (let i of this.healthData) {
					if (i.isEdit)
						return this.$message.warning("请先保存当前编辑项");
				}
				let j = {
					healthTime: "",
					detail: "",
					text: "",
				};
				let k = j;
				k.isEdit = true;

				this.healthData.push(j);
				this.currentData = JSON.parse(JSON.stringify(k));
			},
			readMasterUser() {
				//根据实际情况，自己改下啊
				this.master_user.data.map((i) => {
					i.id = generateId.get(); //模拟后台插入成功后有了id
					return i;
				});
			},
			//修改
			infoChange(row, index, cancel) {
				//点击修改 判断是否已经保存所有操作
				for (let i of this.$data.healthData) {
					if (i.isEdit && i.id != row.id) {
						this.$message.warning("请先保存当前编辑项");
						return false;
					}
				}
				//是否是取消操作
				if (!cancel) {
					if (!this.currentData.id) this.healthData.splice(index, 1);
					return (row.isEdit = !row.isEdit);
				}
				//提交数据
				if (row.isEdit) {
					//项目是模拟请求操作  自己修改下
					let data = JSON.parse(JSON.stringify(this.currentData));
					for (let k in data) {
						row[k] = data[k];
					}
					this.$message({
						type: "success",
						message: "保存成功!",
					});
					//然后这边重新读取表格数据
					// this.readMasterUser();
					row.isEdit = false;
				} else {
					this.currentData = JSON.parse(JSON.stringify(row));
					row.isEdit = true;
				}
			},
			deletInfo(row) {
				for (let i of this.$data.healthData) {
					if (i.isEdit && i.id != row.id) {
						this.$message.warning("请先保存当前编辑项");
						return false;
					}
				}
				// 删除
				this.$confirm("确认删除选中记录吗？", "提示", {
					type: "warning",
				})
					.then(() => {
						this.healthData.forEach((v, i) => {
							if (JSON.stringify(row) === JSON.stringify(v)) {
								var deleted = this.healthData.splice(i, 1);
								console.log("已删除", deleted);
								return;
							}
						});
					})
					.catch(() => {
						console.log("已取消");
					});
			},
			showTag(tagValue) {
				for (let item of this.selectItem) {
					if (tagValue === item["value"]) {
						return item["text"];
					}
				}
			},
		},
		mounted() {
			this.init();
		},
	};
</script>

<style scope>
</style>