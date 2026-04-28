import './assets/main.css'
import PrimeVue from 'primevue/config'
import Aura from '@primevue/themes/aura'
import { createApp } from 'vue'
import App from './App.vue'
import {definePreset} from "@primevue/themes";
import router from "@/router/router.js";

const app = createApp(App)

// overriding PrimeVue Aura theme colors
const InfermedicaPreset = definePreset(Aura, {
    semantic: {
        primary: {
            50: '#eef4ff',
            100: '#d9e6ff',
            200: '#bcd4ff',
            300: '#8ebaff',
            400: '#5a96ff',
            500: '#0062FF', // brand-primary
            600: '#0052db',
            700: '#0040b0',
            800: '#003591',
            900: '#002f74',
            950: '#001d4d'
        }
    }
})

app.use(PrimeVue, {
    theme: {
        preset: InfermedicaPreset,
        options: {
            darkModeSelector: 'none',
        }
    }
})
app.use(router)

app.mount('#app')
