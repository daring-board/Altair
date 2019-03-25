import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Manage from './views/Manage.vue'
import Calender from './views/Calender.vue'
import New from './views/New.vue'
import About from './views/About.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },{
      path: '/manage/:id',
      name: 'manage',
      component: Manage,
      props: true
    },{
      path: '/calender',
      name: 'calender',
      component: Calender
    },{
      path: '/new',
      name: 'new',
      component: New
    },{
      path: '/about',
      name: 'about',
      component: About
    }
  ]
})
