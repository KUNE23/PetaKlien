import { createApp } from 'vue'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import './styles.css'
import App from './App.vue'

createApp(App)
  .use(Toast, {
    position: 'top-right',
    timeout: 3200,
    closeOnClick: true,
    pauseOnHover: true,
  })
  .mount('#app')
