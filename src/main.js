import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './app.css';


// import * as Vue from 'vue' // in Vue 3
import axios from 'axios'
import VueAxios from 'vue-axios'

import 'ant-design-vue/dist/antd.css'; // or 'ant-design-vue/dist/antd.less'

// import { Table, Tag } from 'ant-design-vue';
import Antd from 'ant-design-vue';
import {Chart} from '@antv/g2'


const app = createApp(App)

app.config.globalProperties.$Chart = Chart
app.use(router)
app.use(Antd)
app.use(VueAxios, axios)
app.mount('#app')
