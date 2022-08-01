import { createApp } from 'vue'
import App from './App.vue'
import store from './store'

import './assets/css/tailwind.css'
// import './assets/css/tailwind.output.css'

createApp(App).use(store).mount('#app')
