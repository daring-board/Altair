<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="/">名義管理システム</b-navbar-brand>
      <b-navbar-toggle target="nav_collapse" />
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav>
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
      this.$store.commit('setUserId', '')
      if (this.$route.meta.requiresAuth) {
        this.$router.push({
          path: '/login',
          query: { redirect: this.$route.fullPath }
        })
      }
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
