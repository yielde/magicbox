/*
 * @Author: Galen Tong
 * @Date: 2022-08-02 23:39:31
 * @LastEditTime: 2022-08-04 22:24:12
 * @Description:
 */
import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const router = new VueRouter({
	mode: "history",
	routes: [
		{
			path: "/login",
			name: "Login",
			component: () => import("../views/Login.vue"),
		},
		{
			path: "/",
			name: "Layout",
			component: () => import("../views/Layout.vue"),
			children: [
				{
					path: "",
					redirect: "health",
				},
				{
					path: "health",
					name: "Health",
					component: () => import("../views/health/Health.vue"),
				},
				{
					path: "tools",
					name: "Tools",
					component: () => import("../views/tools/Tools.vue"),
				},
			],
		},
	],
});

export default router;
