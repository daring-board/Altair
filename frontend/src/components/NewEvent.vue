<template>
  <div>
    <div v-if="flag">
      <b-alert variant="success" show>Eventを保存しました。</b-alert>
    </div>
    <b-card header="Create New Event">
      <label for="name">Name</label>
      <b-input id="name" aria-describedby="name-help" required v-model="event.name"/>
      <b-form-text id="name-help">
        Enter the event name in the upper area. 
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
        event: {
          name: null,
        },
        flag: false
      }
    },
    methods: {
      submit(){
        const path = this.$baseURL + `regist_concert`
        axios.post(path, {'concert': this.event})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.flag = true
        })
      }
    }
  }

</script>
