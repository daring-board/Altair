<template>
  <div id="app">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand><div @click="to_home">名義管理システム</div></b-navbar-brand>
      <b-navbar-toggle v-show="is_login" target="nav_collapse" />
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav v-show="is_login" >
          <b-nav-item>
            <router-link class="nav-link" to="/">Home</router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link class="nav-link" to="/calender">Calender</router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link class="nav-link" to="/new">New</router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link class="nav-link" to="/about">About</router-link>
          </b-nav-item>
          <b-nav-item>
            <a @click="logout()" v-if="$store.getters.loggedIn" class="nav-link">Logout</a>
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view/>
    <div v-if="$route.query.message">ログイン認証が必要なページです。</div>
  </div>
</template>

<script>
export default {
  methods: {
    logout () {
      this.$store.commit('auth', '')
      if (this.$route.meta.requiresAuth) {
        this.$router.push({
          path: '/login',
          query: { redirect: this.$route.fullPath }
        })
      }
    },
    to_home() {
      this.$router.push('/')
    },
  },
  computed: {
    is_login: function() {
      if(this.$store.state.accessToken == ''){
        return false
      }
      return true 
    }
  },
  mounted() {

    if (sessionStorage.getItem('accessToken')) {
      this.$store.commit('reload', sessionStorage.getItem('accessToken'))
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
