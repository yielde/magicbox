/*
 * @Author: Galen Tong
 * @Date: 2022-08-10 00:10:38
 * @LastEditTime: 2022-08-10 21:46:49
 * @Description: 
 */
import Vue from 'vue'
import VueCookie from 'vue-cookie'

Vue.use(VueCookie)

export const getUserName = () => {
    return Vue.cookie.get("username")
}

export const setUserToken = (username) => {
    Vue.cookie.set('username', username, {expires: '7D'});
}

export const clearUserToken = () => {
    Vue.cookie.delete('username');
}