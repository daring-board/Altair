<template>
  <div>
    <b-card header="Create New Event">
      <label for="name">Name</label>
      <b-input id="name" aria-describedby="name-help" v-model="event.name"/>
      <b-form-text id="name-help">
        Enter the event name in the upper area. 
      </b-form-text>
      <label for="date">Date</label>
      <datepicker class="text-center" id="date" aria-describedby="date-help" v-model="event.date"></datepicker>
      <b-form-text id="date-help">
        Enter the event date in the upper area. 
      </b-form-text>
      <label for="place">Place</label>
      <b-input id="place" aria-describedby="place-help" v-model="event.place"/>
      <b-form-text id="place-help">
        Enter the event place in the upper area. 
      </b-form-text>
      <b-button variant="primary" @click="submit">Submit</b-button>
    </b-card>
  </div>
</template>

<script>
  import axios from 'axios'
  import datepicker from 'vuejs-datepicker'

  export default {
    data() {
      return {
        event: {
          name: null,
          date: null,
          place: null
        }
      }
    },
    components: {
      datepicker
    },
    methods: {
      submit(){
        const path = this.$baseURL + `regist_concert`
        axios.post(path, {'concert': this.event})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.$router.push({name: 'home'})
        })
      }
    }
  }

</script>
