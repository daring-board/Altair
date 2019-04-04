import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Manage from './views/Manage.vue'
import Calender from './views/Calender.vue'
import New from './views/New.vue'
import About from './views/About.vue'
import Login from './views/Login.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { requiresAuth: true }
    },{
      path: '/manage/:id',
      name: 'manage',
      component: Manage,
      props: true,
      meta: { requiresAuth: true }
    },{
      path: '/calender',
      name: 'calender',
      component: Calender,
      meta: { requiresAuth: true }
    },{
      path: '/new',
      name: 'new',
      component: New,
      meta: { requiresAuth: true }
    },{
      path: '/about',
      name: 'about',
      meta: { isPublic: true },
      component: About
    },{
      path: '/login',
      name: 'login',
      meta: { isPublic: true },
      component: Login
    },{
      path: '*',
      component: Home
    }
  ]
})
