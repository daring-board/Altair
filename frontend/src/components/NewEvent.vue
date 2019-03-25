<template>
  <div>
    <b-card bg-variant="dark" text-variant="white" header="Create New Event">
      <label for="name">Name</label>
      <b-input id="name" aria-describedby="name-help" v-model="event.name"/>
      <b-form-text id="name-help">
        Enter the event name in the upper area. 
      </b-form-text>
      <label for="date">Date</label>
      <b-input id="date" aria-describedby="date-help" v-model="event.date"/>
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
    methods: {
      submit(){
        const path = this.$baseURL + `regist_concert`
        axios.post(path, {name: this.event})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
        })
      }
    }
  }

</script>
