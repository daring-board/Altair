<template>
  <div>
    <div v-if="flag">
      <b-alert variant="success" show>チケットを保存しました。</b-alert>
    </div>
    <b-card header="Create New Ticket">
      
      <label for="select-schedule">Select Schedule</label>
      <b-form-select id="select-schedule" aria-describedby="schedule-help" :options="s_options" required v-model="form.schedule" />
      <b-form-text id="schedule-help">
        チケットの申し込みを行うイベントを選択する
      </b-form-text>

      <label for="select-member">Event Member</label>
      <b-form-select id="select-member" aria-describedby="member-help" :options="m_options" required v-model="form.member" />
      <b-form-text id="member-help">
        チケットの申し込みを行う名義を選択する
      </b-form-text>

      <label for="num">Time</label>
      <b-form-input class="text-center" id="num" :type="`number`" aria-describedby="num-help" required v-model="form.number"></b-form-input>
      <b-form-text id="num-help">
        Enter the ticket number in the upper area. 
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
        s_options: [{ text: 'Select Schedule', value: null }, ],
        m_options: [{ text: 'Select Member', value: null }, ],
        form: {
          schedule: null,
          member: null,
          number: 0,
        },
        flag: false
      }
    },
    methods: {
      submit(){
        const path = this.$baseURL + `regist_ticket`
        axios.post(path, {'ticket': this.form})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.flag = true
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
                value: member
              })
            })
            /* eslint-disable */
            console.log(this.members)
            console.log(this.m_options)
          })
      },
      getSchedules(){
        const path = this.$baseURL + `schedules`
        axios.get(path)
          .then(response => {
            this.schedules = response.data
            response.data.forEach((schedule) => {
              const c_path = this.$baseURL + `concert/` + schedule.concert_id
              axios.get(c_path)
                .then(res => {
                  this.s_options.push({
                    text: res.data.name + ' ' + schedule.date + ' ' + schedule.time,
                    value: schedule
                  }) 
              })
            })
            /* eslint-disable */
            console.log(response.data)
            console.log(this.s_options)
          })
      }
    },
    created: function() {
      this.getMembers()
      this.getSchedules()
    }
  }

</script>
