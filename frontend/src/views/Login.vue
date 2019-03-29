<template>
  <div class="login">
    <h1>This is an login page</h1>
    <input v-model="userId"/>
    <button @click="login()" :disabled="!userId">ログイン</button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      userId: ''
    }
  },
  methods: {
    login () {
      this.$store.commit('setUserId', this.userId)
      this.$router.push(this.$route.query.redirect)
    }
  }
}
</script>
