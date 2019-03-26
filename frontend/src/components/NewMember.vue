<template>
  <div>
    <b-card header="Create New Member">
      <label for="member-name">Name</label>
      <b-form-input id="member-name" aria-describedby="member-name-help" v-model="member_name"/>
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
        member_name: null
      }
    },
    methods: {
      submit(){
        const path = this.$baseURL + `regist_member`
        axios.post(path, {'name': this.member_name})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.$router.push({name: 'home'})
        })
      }
    }
  }

</script>
