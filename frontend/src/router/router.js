import { createRouter, createWebHistory } from 'vue-router'
import Interview from "@/pages/Interview.vue";

const routes = [
  {
    path: '/',
    name: 'Start',
    component: Interview
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