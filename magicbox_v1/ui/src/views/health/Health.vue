<!--
 * @Author: Galen Tong
 * @Date: 2022-08-04 22:16:32
 * @LastEditTime: 2022-08-14 14:20:34
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
							prop: 'time',
							order: 'descending',
						}"
					>
						<el-table-column label="ID" prop="id" v-if="false">
						</el-table-column>
						<el-table-column type="index" label="序号">
						</el-table-column>
						<el-table-column prop="time" label="时间" sortable>
							<template slot-scope="scope">
								<span v-if="scope.row.isEdit">
									<el-date-picker
										v-model="currentData['time']"
										type="datetime"
										format="yyyy-MM-dd HH:mm:ss"
										value-format="yyyy-MM-dd HH:mm:ss"
										placeholder="选择日期时间"
										align="right"
										:picker-options="pickerOptions"
									>
									</el-date-picker>
								</span>
								<span v-else>
									{{ scope.row.time }}
								</span>
							</template>
						</el-table-column>

						<el-table-column
							prop="health_detail"
							label="详细信息"
							sortable
						>
							<template slot-scope="scope">
								<span v-if="scope.row.isEdit">
									<el-input
										v-model="currentData['health_detail']"
										placeholder="输入内容"
									>
									</el-input>
								</span>
								<span v-else>
									{{ scope.row.health_detail }}
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
								<span v-else style="border: 0px; padding: 0px">
									<el-tag
										v-if="scope.row.text === 1"
										type="success"
										>{{ showTag(scope.row.text) }}</el-tag
									>
									<el-tag
										v-else-if="scope.row.text === 2"
										type="warning"
										>{{ showTag(scope.row.text) }}</el-tag
									>
									<el-tag
										v-else-if="scope.row.text === 3"
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
	export default {
		name: "Health",

		data() {
			return {
				default_time: null,
				searchForm: {
					title: "",
					category: "",
					dateValue: "",
				},
				selectItem: [
					{ text: "轻微", value: 1 },
					{ text: "中等", value: 2 },
					{ text: "严重", value: 3 },
				],
				healthColumns: [
					{ prop: "id", label: "ID" },
					{ prop: "time", label: "时间" },
					{ prop: "health_detail", label: "详细信息" },
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
				const loading = this.$loading();
				this.axios.get("/health/").then((res) => {
					loading.close();
					if (res.data.code === 0) {
						res.data.data.forEach((row) => {
							row.isEdit = false;
						});
						this.healthData = res.data.data;
					} else {
						this.$message.error("请求失败");
					}
				});
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
			addHealthInfo() {
				for (let i of this.healthData) {
					if (i.isEdit)
						return this.$message.warning("请先保存当前编辑项");
				}
				let j = {
					id: null,
					time: "",
					health_detail: "",
					text: "",
				};
				let k = j;
				j.isEdit = true;
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
					if (this.currentData["time"] === "") {
						this.currentData["time"] = jutils.formatDate(
							new Date(),
							"YYYY-MM-DD HH:ii:ss"
						);
					}
					let data = JSON.parse(JSON.stringify(this.currentData));
					if (!data.id) {
						this.axios.post("/health/", data).then((res) => {
							console.log(data);
							if (res.data.code === 0) {
								this.$message({
									type: "success",
									message: "保存成功!",
								});
								res.data.data.isEdit = false;
								for (let k in res.data.data) {
									row[k] = res.data.data[k];
								}
								return;
							}
							if (res.data.code === 1001) {
								let offset = 0;
								console.log(res.data);
								for (let i in res.data.detail) {
									for (let j of res.data.detail[i]) {
										this.$message({
											message: j,
											type: "error",
											center: true,
											offset: offset * 60,
											showClose: true,
											duration: 2000,
										});
										offset += 1;
									}
								}
								this.init();
								return;
							} else {
								this.$message.error("请求错误");
							}
						});
					} else {
						this.axios.put(`/health/${data.id}/`, data).then((res) => {
							if (res.data.code === 0) {
								this.$message({
									type: "success",
									message: "保存成功!",
								});
								res.data.data.isEdit = false;
								for (let k in res.data.data) {
									row[k] = res.data.data[k];
								}
								return;
							}
							if (res.data.code === 1001) {
								let offset = 0;
								for (let i in res.data.detail) {
									for (let j of res.data.detail[i]) {
										this.$message({
											message: j,
											type: "error",
											center: true,
											offset: offset * 60,
											showClose: true,
											duration: 2000,
										});
										offset += 1;
									}
								}
								return;
							} else {
								this.$message.error("请求错误");
							}
						});
					}

					row.isEdit = false;
				} else {
					this.currentData = JSON.parse(JSON.stringify(row));
					this.currentData["time"] = jutils.formatDate(
						new Date(this.currentData["time"]),
						"YYYY-MM-DD HH:ii:ss"
					);
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
				this.currentData = JSON.parse(JSON.stringify(row));
				// 删除
				this.$confirm("确认删除选中记录吗？", "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning",
				}).then(() => {
						this.axios
							.delete(`/health/${this.currentData.id}/`)
							.then((res) => {
                                console.log(res.data)
								if (res.data.code === 0) {
									this.$message({
										type: "success",
										message: res.data.data,
									});
                                    this.init();
									return;
								}
								if (res.data.code === 2001) {
									this.$message({
										type: "error",
										message: res.data.detail,
									});
                                    this.init();
									return;
								} else {
									this.$message.error("请求错误");
                                    this.init();
								}
							});
					}).catch(()=>{
                        this.$message.warning("取消删除")
                    })

			},
			showTag(tagValue) {
				for (let item of this.selectItem) {
					if (tagValue === item["value"]) {
						return item["text"];
					}
				}
			},
		},
		created() {
			this.init();
		},
		mounted() {},
	};
</script>

<style scope>
</style>