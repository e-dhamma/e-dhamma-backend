// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'

import App from './App'
import router from './router'
import { store } from './store'
import DataFilter from './filters/date'

Vue.filter('date', DataFilter)

Vue.use(Vuetify, { theme: {
  primary: '#cd5a07',
  secondary: '#424242',
  accent: '#82B1FF',
  error: '#FF5252',
  info: '#2196F3',
  success: '#4CAF50',
  warning: '#FFC107'
}})

Vue.config.productionTip = false

/* eslint-disable no-new */
export const bus = new Vue()

new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
