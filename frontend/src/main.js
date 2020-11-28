import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ApiService from '@/services/api'

import './buefy'
import './assets/style/base.scss'

const API_PATH = 'https://oxigen.banatit.ro/api/'
ApiService.init(API_PATH)

// filters

let currencyFormatter = new Intl.NumberFormat('ro-RO', {
  style: 'currency',
  currency: 'lei',
  currencyDisplay: 'symbol'
})

Vue.filter('currency', function(value) {
  if (!value) return '0'
  return currencyFormatter.format(String(value)).replace('LEI', 'lei')
})

//

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
