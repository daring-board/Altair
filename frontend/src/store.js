import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: ''
  },
  getters: {
    loggedIn: state => {
      /* eslint-disable */
      console.log(Boolean(state.accessToken))
      return Boolean(state.accessToken)
    }
  },
  mutations: {
    auth(state, user) {
      if(user == '') {
        state.accessToken = ''
        sessionStorage.setItem('accessToken', state.accessToken);
        return
      }
      const path = Vue.prototype.$baseURL.replace('api/', '') + `auth`
      axios.post(path, {'username': user.username, 'password': user.password})
      .then(response => {
        /* eslint-disable */
        // console.log(response.data['access_token'])
        state.accessToken = response.data['access_token']
        sessionStorage.setItem('accessToken', state.accessToken);
        router.push('/')
      })
    },
    reload(state, token) {
      state.accessToken = token
      router.push('/')
    }
  },
  actions: {

  },
})