/*
 * @Author: Galen Tong
 * @Date: 2022-08-03 22:39:01
 * @LastEditTime: 2022-08-10 21:45:23
 * @Description:
 */
import Vue from "vue";
import Vuex from "vuex";
import { clearUserToken, getUserName, setUserToken } from "@/plugins/cookie";

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		username: getUserName(),
	},
	mutations: {
		login: function (state, { username }) {
			state.username = username;
			setUserToken(username);
		},
		logout: function (state) {
			state.username = "";
			clearUserToken();
		},
	},
	actions: {},
	modules: {},
});
