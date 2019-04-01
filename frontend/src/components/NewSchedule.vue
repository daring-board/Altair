<template>
  <div>
    <div v-if="flag">
      <b-alert variant="success" show>Scheduleを保存しました。</b-alert>
    </div>
    <b-card header="Create New Schedule">
      <label for="select-event">Event Name</label>
      <b-form-select id="select-event" aria-describedby="event-help" :options="e_options" required v-model="form.concert" />
      <b-form-text id="event-help">
        コンサート名を選択する
      </b-form-text>

      <label for="date">Date</label>
      <b-form-input class="text-center" id="date" :type="`date`" aria-describedby="date-help" required v-model="form.date"></b-form-input>
      <b-form-text id="date-help">
        Enter the event date in the upper area. 
      </b-form-text>

      <label for="time">Time</label>
      <b-form-input class="text-center" id="time" :type="`time`" aria-describedby="time-help" required v-model="form.time"></b-form-input>
      <b-form-text id="time-help">
        Enter the event time in the upper area. 
      </b-form-text>
      
      <label for="place">Place</label>
      <b-input id="place" aria-describedby="place-help" required v-model="form.place"/>
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
        flag: false,
        form: {
          concert: null,
          date: null,
          time: null,
          place: null,
        },
        e_options: [{ text: 'Select Event', value: null }, ],
      }
    },
    methods: {
      submit(){
        const path = this.$baseURL + `regist_schedule`
        axios.post(path, {'schedule': this.form},
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.flag = true
        })
      },
      getConcerts(){
        const path = this.$baseURL + `concerts`
        axios.get(path,
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            this.concerts = response.data
            response.data.forEach((concert) => { 
              this.e_options.push({
                text: concert.name,
                value: concert
              }) 
            })
            /* eslint-disable */
            console.log(response.data)
            console.log(this.e_options)
          })
      }
    },
    created: function() {
      this.getConcerts()
    }
  }

</script>
