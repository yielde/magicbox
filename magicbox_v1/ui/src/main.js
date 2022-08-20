/*
 * @Author: Galen Tong
 * @Date: 2022-08-02 22:53:42
 * @LastEditTime: 2022-08-14 16:53:09
 * @Description:
 */
import Vue  from "vue"
import HighchartsVue from "highcharts-vue"
import App from "./App.vue"
import router from "./router"
import store from "./store"
import './plugins/axios'
import './plugins/cookie'
import './plugins/element'

Vue.config.productionTip = false;

Vue.use(HighchartsVue)

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')