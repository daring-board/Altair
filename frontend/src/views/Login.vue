<template>
  <div class="login">
    <b-container fluid>
      <h2 style="padding:10px">ユーザー名とパスワードを入力</h2>
      <b-row>
        <b-col sm="1"></b-col>
        <b-col sm="3">
          <label for="name">UserName:</label>
        </b-col>
        <b-col sm="7">
          <b-form-input
            id="name" 
            type="text"
            :state="userNameValidate"
            v-model="user.username"
            aria-describedby="input-validate"
          />
          <b-form-invalid-feedback id="input-validate">
            ユーザー名が入力されていません
          </b-form-invalid-feedback>
        </b-col>
        <b-col sm="1"></b-col>
      </b-row>
      <br/>
      <b-row>
        <b-col sm="1"></b-col>
        <b-col sm="3">
          <label for="pwd">Password:</label>
        </b-col>
        <b-col sm="7">
          <b-form-input id="pwd" type="password" v-model="user.password"/>
        </b-col>
        <b-col sm="1"></b-col>
      </b-row>
      <br/>
      <b-row>
        <b-col sm="8"></b-col>
        <b-col sm="3">
          <b-button variant="outline-primary" @click="login()" :disabled="!user.username">ログイン</b-button>
        </b-col>
        <b-col sm="1"></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user: {
        username: '',
        password: ''
      }
    }
  },
  computed: {
    userNameValidate() {
      /* eslint-disable */
      console.log(/\S/g.exec(this.user.username))
      return /\S/g.exec(this.user.username)? true: false
    }
  },
  methods: {
    login () {
      this.$store.commit('auth', this.user)
    }
  }
}
</script>
