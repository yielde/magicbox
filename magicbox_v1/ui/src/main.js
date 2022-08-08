/*
 * @Author: Galen Tong
 * @Date: 2022-08-02 22:53:42
 * @LastEditTime: 2022-08-03 23:36:14
 * @Description:
 */
import Vue  from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store"

import "./plugins/element";

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')