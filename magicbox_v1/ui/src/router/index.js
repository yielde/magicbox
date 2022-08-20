/*
 * @Author: Galen Tong
 * @Date: 2022-08-02 23:39:31
 * @LastEditTime: 2022-08-20 17:53:40
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
			path: "/registry",
			name: "Registry",
			component: () => import("../views/Registry.vue"),
		},
		{
			path: "/",
			name: "Layout",
			component: () => import("../views/Layout.vue"),
			children: [
				{
					path: "/",
					redirect: "healthlayout",
				},
				{
					path: "healthlayout",
					name: "HealthLayout",
					component: () => import("../views/health/HealthLayout.vue"),
                    children:[
                        {
                            path:"/",
                            redirect:"health"
                        },
                        {
                            path:"health",
                            name:"Health",
                            component:()=> import("../views/health/Health.vue")
                        },
                        {
                            path:"stastic",
                            name:"Stastic",
                            component:()=> import("../views/health/Stastic.vue")
                        }
                    ]
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
