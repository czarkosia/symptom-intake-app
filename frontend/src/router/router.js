import { createRouter, createWebHistory } from 'vue-router'
import InterviewStart from '../components/Start.vue'

const routes = [
  {
    path: '/',
    name: 'Start',
    component: InterviewStart
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../components/banners/NotFoundBanner.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router