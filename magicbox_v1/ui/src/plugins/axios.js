/*
 * @Author: Galen Tong
 * @Date: 2022-08-09 23:41:25
 * @LastEditTime: 2022-08-09 23:42:29
 * @Description: 
 */
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from '../router/index'
import {Message} from "element-ui"


Vue.use(VueAxios, axios)

axios.defaults.baseURL = 'http://172.17.73.129:8888/api/'