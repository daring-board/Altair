<template>
  <div>
    <div v-if="flag">
      <b-alert variant="success" show>Memberを保存しました。</b-alert>
    </div>
    <b-card header="Create New Member">
      <label for="member-name">Name</label>
      <b-form-input id="member-name" aria-describedby="member-name-help" required v-model="member_name"/>
      <b-form-text id="member-name-help">
        Input name of new member, and push following button. 
      </b-form-text>
      <b-button variant="primary" @click="submit">Submit</b-button>
    </b-card>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        member_name: null,
        flag: false
      }
    },
    methods: {
      submit(){
        const path = this.$baseURL + `regist_member`
        axios.post(path, {'name': this.member_name})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.flag = true
        })
      }
    }
  }

</script>
