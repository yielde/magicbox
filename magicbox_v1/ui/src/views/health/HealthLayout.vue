<!--
 * @Author: Galen Tong
 * @Date: 2022-08-20 16:45:53
 * @LastEditTime: 2022-08-20 18:01:14
 * @Description: 
-->
<template>
	<div>
		<el-menu
			class="sub-menu"
			mode="horizontal"
			:default-active="subActiveRouter"
			router
		>
			<el-menu-item index="Health" :route="{ name: 'Health' }"
				>信息记录</el-menu-item
			>
			<el-menu-item index="Stastic" :route="{ name: 'Stastic' }"
				>信息统计</el-menu-item
			>
		</el-menu>

		<router-view></router-view>
	</div>
</template>

<script>
	export default {
		name: "HealthLayout",
		data() {
			return {
				subActiveRouter: "",
			};
		},
        watch:{
            $route:function(to) {
                this.subActiveRouter = to.name;
            }
        },
		mounted() {
			// 获取当前的所有路由
			this.subActiveRouter = this.$route.matched[2].name;
		},
	};
</script>

<style scoped>
	.sub-menu .el-menu-item {
		line-height: 40px;
		height: 40px;
		vertical-align: middle;
		font-size: 13px;
	}

	.sub-menu .el-menu-item i {
		margin-top: -3px;
	}
</style>