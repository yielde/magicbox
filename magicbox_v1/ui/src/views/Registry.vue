<!--
 * @Author: Galen Tong
 * @Date: 2022-08-09 22:06:26
 * @LastEditTime: 2022-08-10 22:40:10
 * @Description: 
-->
<template>
	<div class="main">
		<el-card class="box-card">
			<div class="registryBox">
				<div class="tabBoxSwitch">
					<ul class="tabBoxSwitchUl">
						<li class="tab-active">
							<i class="el-icon-user"></i> 注册
						</li>
					</ul>
				</div>
				<div>
					<el-form
						:model="registryForm"
						:rules="registryRules"
						ref="registryForm"
					>
						<el-form-item
							prop="username"
							:error="registryFormError.username"
							style="margin-top: 24px"
						>
							<el-input
								v-model="registryForm.username"
								placeholder="用户名或手机号"
							>
							</el-input>
						</el-form-item>
						<el-form-item
							prop="email"
							:error="registryFormError.email"
							style="margin-top: 24px"
						>
							<el-input
								v-model="registryForm.email"
								placeholder="邮箱"
							>
							</el-input>
						</el-form-item>

						<el-form-item
							prop="password"
							:error="registryFormError.password"
						>
							<el-input
								v-model="registryForm.password"
								placeholder="密码"
								show-password
							></el-input>
						</el-form-item>
						<el-form-item
							prop="confirm_password"
							:error="registryFormError.confirm_password"
						>
							<el-input
								v-model="registryForm.confirm_password"
								placeholder="确认密码"
								show-password
							></el-input>
						</el-form-item>
						<el-form-item class="btn">
							<el-button
								type="primary"
								size="medium"
								@click="toLogin()"
							>
								<i class="el-icon-position"></i> 去登录
							</el-button>
							<el-button
								type="success"
								size="medium"
								@click="submitRegistry('registryForm')"
							>
								注 册
							</el-button>
						</el-form-item>
					</el-form>
				</div>
			</div>
		</el-card>
	</div>
</template>

<script>
	export default {
		name: "Registry",
		data() {
			return {
				registryForm: {
					username: "",
					password: "",
					email: "",
					confirm_password: "",
				},
				registryFormError: {
					username: "",
					password: "",
					email: "",
					confirm_password: "",
				},
				registryRules: {
					username: [
						{
							required: true,
							message: "请输入用户名或手机",
							trigger: "blur",
						},
					],
					email: [
						{ required: true, message: "请输入邮箱", trigger: "blur" },
						{
							pattern:
								/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/,
							message: "请输入正确的邮箱格式",
							trigger: "blur",
						},
					],
					password: [
						{ required: true, message: "请输入密码", trigger: "blur" },
					],
					confirm_password: [
						{ required: true, message: "请确认密码", trigger: "blur" },
					],
				},
			};
		},
		methods: {
			submitRegistry(formName) {
				this.clearRegistryFormError();
				this.$refs[formName].validate((valid) => {
					if (!valid) {
						return false;
					}

					this.axios.post("/registry/", this.registryForm).then((res) => {
						console.log(res.data);
						if (res.data.code === 0) {
							this.$store.commit("login", res.data.data);
							this.$router.push("/");
							return;
						}
						if (res.data.code === 1000) {
							this.validateFormFailed(res.data.detail);
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
						} else {
							this.$message.error("请求失败");
						}
					});
				});
			},
			clearRegistryFormError() {
				for (let key in this.registryFormError) {
					this.registryFormError[key] = "";
				}
			},
			toLogin() {
				this.$router.push("Login");
			},
		},
	};
</script>

<style scope>
	.main {
		width: 100%;
		height: 100vh;
		background-color: #42647e9d;

		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.registryBox {
		background-color: #ffffff;
		box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);
		border-radius: 2px;
		width: 380px;
		min-height: 200px;
		padding: 0 24px 20px;
	}

	.btn {
		display: flex;
		justify-content: flex-end;
	}
	.registryBox {
		background-color: #ffffff;
		box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);
		border-radius: 2px;
		width: 380px;
		min-height: 200px;
		padding: 0 24px 20px;
	}
	.tabBoxSwitch .tabBoxSwitchUl {
		list-style: none;
		padding: 0;
		margin: 0;
	}

	.tabBoxSwitch .tabBoxSwitchUl li {
		display: inline-block;
		height: 60px;
		font-size: 16px;
		line-height: 60px;
		margin-right: 24px;
		cursor: pointer;
	}
	.tab-active::before {
		display: block;
		position: absolute;
		bottom: 0;
		content: "";
		width: 100%;
		height: 3px;
		background-color: #0084ff;
	}
	.tab-active {
		position: relative;
		color: #1a1a1a;
		font-weight: 600;
		font-synthesis: style;
	}
</style>