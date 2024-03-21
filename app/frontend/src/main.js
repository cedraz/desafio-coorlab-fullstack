import { createApp } from 'vue'
import App from './App.vue'
import PhosphorIcons from "@phosphor-icons/vue"
import './index.css'

const app = createApp(App)

app.use(PhosphorIcons)

app.mount('#app')
