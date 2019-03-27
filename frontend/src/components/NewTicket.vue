<template>
  <div>
    <b-card header="Create New Ticket">
      <label for="select-event">Event Name</label>
      <b-form-select id="select-event" aria-describedby="event-help" :options="e_options" required v-model="form.event" />
      <b-form-text id="event-help">
        チケットの申し込みを行うイベントを選択する
      </b-form-text>
      <label for="select-member">Event Member</label>
      <b-form-select id="select-member" aria-describedby="member-help" :options="m_options" required v-model="form.member" />
      <b-form-text id="member-help">
        チケットの申し込みを行う名義を選択する
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
        e_options: [{ text: 'Select Event', value: null }, ],
        m_options: [{ text: 'Select Member', value: null }, ],
        form: {
          event: null,
          member: null,
        }
      }
    },
    methods: {
      submit(){
        const path = this.$baseURL + `regist_ticket`
        axios.post(path, {'ticket': this.form})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.$emit('success', 'チケットを保存しました。')
        })
      },
      getMembers(){
        const path = this.$baseURL + `members`
        axios.get(path)
          .then(response => {
            this.members = response.data
            response.data.forEach((member) => {
              this.m_options.push({
                text: member.name,
                value: member}
                )
            })
            /* eslint-disable */
            console.log(this.members)
            console.log(this.m_options)
          })
      },
      getConcerts(){
        const path = this.$baseURL + `concerts`
        axios.get(path)
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
      this.getMembers()
      this.getConcerts()
    }
  }

</script>
