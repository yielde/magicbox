<!--
 * @Author: Galen Tong
 * @Date: 2022-08-04 22:04:24
 * @LastEditTime: 2022-08-10 21:47:20
 * @Description: 
-->
<template>
	<div class="home">
		<div class="home">
			<el-menu
				class="el-menu-demo"
				mode="horizontal"
				:default-active="rootActiveRouter"
				background-color="#545c64"
				text-color="#fff"
				active-text-color="#ffd04b"
				router
			>
				<el-menu-item>MagicBox</el-menu-item>
				<el-menu-item index="Health" :route="{ name: 'Health' }"
					>健康记录</el-menu-item
				>
				<el-menu-item index="Tools" :route="{ name: 'Tools' }"
					>工具</el-menu-item
				>
				<el-submenu index="userinfo" style="float: right">
					<template slot="title">{{ username }}</template>
					<el-menu-item index="userinfo-info">个人信息</el-menu-item>
					<el-menu-item index="userinfo-change-passwd"
						>修改密码</el-menu-item
					>
					<el-menu-item index="userinfo-logout" @click="logout()"
						>注销</el-menu-item
					>
				</el-submenu>
			</el-menu>
		</div>
		<div>
			<router-view></router-view>
		</div>
	</div>
</template>

<script>
	export default {
		name: "Layout",
		data() {
			return {
				rootActiveRouter: "",
			};
		},
		mounted() {
			console.log(this.$route.matched[1]);
			this.rootActiveRouter = this.$route.matched[1].name;
		},
		computed: {
			username() {
				return this.$store.state.username;
			},
		},
		methods: {
			logout() {
                this.$store.commit("logout");
                this.$router.push("Login");
                return
            },
		},
	};
</script>

<style>
</style>