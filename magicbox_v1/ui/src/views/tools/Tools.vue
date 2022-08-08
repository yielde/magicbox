<!--
 * @Author: Galen Tong
 * @Date: 2022-08-04 22:16:32
 * @LastEditTime: 2022-08-07 16:26:58
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
						:data="master_user.data"
						border
						style="width: 100%"
						highlight-current-row
					>
						<el-table-column type="index" label="序号" sortable></el-table-column>

						<el-table-column
							v-for="(v, i) in master_user.columns"
							:prop="v.field"
							:label="v.title"
							:width="v.width"
							:key="i"
                            sortable
						>
							<template slot-scope="scope">
								<span v-if="scope.row.isSet">
									<el-input
										size="mini"
										placeholder="请输入内容"
										v-model="master_user.sel[v.field]"
									>
									</el-input>
								</span>
								<span v-else>{{ scope.row[v.field] }}</span>
							</template>
						</el-table-column>
                        
						<el-table-column label="操作" width="100">
							<template slot-scope="scope">
								<span
									class="el-tag el-tag--info el-tag--mini"
									style="cursor: pointer"
									@click="
										pwdChange(scope.row, scope.$index, true)
									"
								>
									{{ scope.row.isSet ? "保存" : "修改" }}
								</span>
								<span
									v-if="!scope.row.isSet"
									class="el-tag el-tag--danger el-tag--mini"
									style="cursor: pointer"
								>
									删除
								</span>
								<span
									v-else
									class="el-tag el-tag--mini"
									style="cursor: pointer"
									@click="
										pwdChange(
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
						@click="addMasterUser()"
					>
						<span>+ 添加</span>
					</el-button>
				</el-col>
			</el-row>
		</el-card>
	</div>
</template>

<script>
	//id生成工具 这个不用看 示例而已 模拟后台返回的id
	var generateId = {
		_count: 1,
		get() {
			return +new Date() + "_" + this._count++;
		},
	};
	export default {
		name: "Tools",
		data() {
			return {
				searchForm: {
					title: "",
					category: "",
					dateValue: "",
				},
				master_user: {
					sel: null, //选中行
					columns: [
						{ field: "type", title: "远程类型", width: 120 },
						{ field: "addport", title: "连接地址", width: 150 },
						{ field: "user", title: "登录用户", width: 120 },
						{ field: "pwd", title: "登录密码", width: 220 },
						{ field: "info", title: "其他信息" },
					],
					data: [],
				},
			};
		},
		methods: {
            clickSearch() {
                console.log(this.searchForm)
            },
            resetSearchForm(formName) {
                this.$refs[formName].resetFields();
            },
			//读取表格数据
			readMasterUser() {
				//根据实际情况，自己改下啊
				this.master_user.data.map((i) => {
					i.id = generateId.get(); //模拟后台插入成功后有了id
					return i;
				});
			},
			//添加账号
			addMasterUser() {
				for (let i of this.master_user.data) {
					if (i.isSet) return this.$message.warning("请先保存当前编辑项");
				}
				let j = {
					id: 0,
					type: "",
					addport: "",
					user: "",
					pwd: "",
					info: "",
					isSet: true,
					_temporary: true,
				};
				this.master_user.data.push(j);
                console.log(j)
				this.master_user.sel = JSON.parse(JSON.stringify(j));
			},
			//修改
			pwdChange(row, index, cg) {
				//点击修改 判断是否已经保存所有操作
				for (let i of this.$data.master_user.data) {
					if (i.isSet && i.id != row.id) {
						this.$message.warning("请先保存当前编辑项");
						return false;
					}
				}
				//是否是取消操作
				if (!cg) {
					if (!this.master_user.sel.id)
                        console.log(this.master_user.sel.id);
						this.master_user.data.splice(index, 1);
					return (row.isSet = !row.isSet);
				}
				//提交数据
				if (row.isSet) {
					//项目是模拟请求操作  自己修改下
					let data = JSON.parse(JSON.stringify(this.master_user.sel));
					for (let k in data) {
						row[k] = data[k];
					}
					this.$message({
						type: "success",
						message: "保存成功!",
					});
					//然后这边重新读取表格数据
					// this.readMasterUser();
					row.isSet = false;
				} else {
					this.master_user.sel = JSON.parse(JSON.stringify(row));
					row.isSet = true;
				}
			},
		},
	};
</script>

<style scope>
</style>