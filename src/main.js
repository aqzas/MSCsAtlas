import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './app.css';


// import * as Vue from 'vue' // in Vue 3
import axios from 'axios'
import VueAxios from 'vue-axios'

import { Runtime, extend, corelib } from '@antv/g2'
const Chart = extend(Runtime, corelib());


const app = createApp(App)

app.config.globalProperties.$Chart = Chart
// app.config.globalProperties.$BasePath = "http://bioinfo.life.hust.edu.cn/MSCapi"
app.config.globalProperties.$BasePath = "https://msc.unioncell.cn/MSCapi"
app.use(router)
app.use(VueAxios, axios)
app.mount('#app')
