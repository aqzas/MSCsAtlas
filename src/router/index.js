import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import("../views/HomeView.vue")
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import("../views/DashboardView.vue")
    },
    {
      path: '/expression',
      name: 'expression',
      component: () => import("../views/Expression.vue")
    },
    {
      path: '/enrichment',
      name: 'enrichment',
      component: () => import("../views/Enrichment.vue")
    },
    {
      path: '/assess',
      name: 'assess',
      component: () => import("../views/Assess.vue")
    },
    {
      path: '/playground',
      name: 'playground',
      component: () => import("../views/Playground.vue")
    },
  ]
})

export default router
