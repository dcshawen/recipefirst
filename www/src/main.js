import { createApp } from 'vue'
import router from './routes.js'
import App from './App.vue'

import 'vuetify/styles'

import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi'
  },
})

createApp(App).use(router).use(vuetify).mount('#app')
