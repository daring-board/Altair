<template>
  <div>
    <b-button variant="primary" style="float: right" v-b-modal.add-event @click="changeEvtTitle('イベント追加')"><b-badge variant="light">+</b-badge></b-button>
    <div v-for="concert in concerts" v-bind:key="concert.id">
      <div>
        <h3 style='text-align: left; margin-left: 10px; float: left'>{{concert.name}}</h3>
        <b-button class="edit-title" v-b-modal.add-event @click="selectEvt(concert, 'イベント名変更')">
          <i class="fas fa-edit"></i>
        </b-button>
      </div>
      <b-table striped hover :items="schedules[concert.id]" :fields="fields">
        <template slot="edit" slot-scope="data">
          <div v-if="data.item.edit != 'Add'">
            <b-button v-b-modal.edit-modal @click="setObj(data.item)">
              <i class="fas fa-edit"></i>
            </b-button>
          </div>
          <div v-else>
            <b-button style="margin-bottom:15px;" v-b-modal.add-schedule @click="schedule.concert = concert">
              <i class="fas fa-plus"></i>
            </b-button>
          </div>
        </template>
      </b-table>
    </div>
    <!-- チケット編集モーダル -->
    <b-modal
      id="edit-modal"
      ref="e_modal"
      @ok="editOk"
      @cancel="cancelModel"
    >
      <div slot="modal-header">
        チケット編集
      </div>
      <form @submit.stop.prevent="editOk">
        <label for="date">Date</label>
        <b-form-input class="text-center" id="date" :type="`date`" :state="checkEditDate" aria-describedby="date-help" required v-model="edit_form.date"></b-form-input>
        <b-form-text id="date-help">
          Enter the event date in the upper area. 
        </b-form-text>

        <label for="time">Time</label>
        <b-form-input class="text-center" id="time" :type="`time`" :state="checkEditTime" aria-describedby="time-help" required v-model="edit_form.time"></b-form-input>
        <b-form-text id="time-help">
          Enter the event time in the upper area. 
        </b-form-text>
        
        <label for="place">Place</label>
        <b-input id="place" aria-describedby="place-help" :state="checkEditPlace" required v-model="edit_form.place"/>
        <b-form-text id="place-help">
          Enter the event place in the upper area. 
        </b-form-text>

        <label for="num">Number of Ticket</label>
        <b-input id="num" aria-describedby="num-help" :type="`number`" :state="checkEditNumber" required v-model="edit_form.num"/>
        <b-form-text id="num-help">
          Enter the Number of Ticket in the upper area. 
        </b-form-text>

        <label for="status">Status</label>
        <b-form-select id="status" aria-describedby="status-help" :options="options" :state="checkEditState" required v-model="edit_form.status"/>
        <b-form-text id="status-help">
          Select status in the upper area. 
        </b-form-text>
      </form>
    </b-modal>
    <!-- チケット追加モーダル -->
     <b-modal
      id="add-schedule"
      ref="s_modal"
      @ok="addSchedule"
      @cancel="cancelModel"
    >
      <div slot="modal-header">
        スケジュール追加
      </div>
      <form @submit.stop.prevent="addSchedule">
        <label for="select-event">Event Name</label>
        <b-form-select id="select-event" aria-describedby="event-help" :options="e_options" :state="checkSchName" required v-model="schedule.concert"/>
        <b-form-text id="event-help">
          コンサート名を選択する
        </b-form-text>

        <label for="date">Date</label>
        <b-form-input class="text-center" id="date" :type="`date`" aria-describedby="date-help" :state="checkSchDate" required v-model="schedule.date"></b-form-input>
        <b-form-text id="date-help">
          Enter the event date in the upper area. 
        </b-form-text>

        <label for="time">Time</label>
        <b-form-input class="text-center" id="time" :type="`time`" aria-describedby="time-help" :state="checkSchTime" required v-model="schedule.time"></b-form-input>
        <b-form-text id="time-help">
          Enter the event time in the upper area. 
        </b-form-text>
        
        <label for="place">Place</label>
        <b-input id="place" aria-describedby="place-help" :state="checkSchPlace" required v-model="schedule.place"/>
        <b-form-text id="place-help">
          Enter the event place in the upper area. 
        </b-form-text>
      </form>
    </b-modal>
    <!-- イベント追加モーダル -->
    <b-modal
      id="add-event"
      ref="modal"
      @ok="addOk"
      @cancel="cancelEventModal"
    >
      <div slot="modal-header">
        {{event_modal_title}}
      </div>
      <form @submit.stop.prevent="addOk">
        <label for="event-name">Name</label>
        <b-form-input id="event-name" aria-describedby="event-name-help" :state="checkEventName" v-model="event.name"/>
        <b-form-text id="event-name-help">
          Input name of new event, and push following button. 
        </b-form-text>
      </form>
    </b-modal>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        // Note `isActive` is left out and will not appear in the rendered table
        fields: [
          {key: 'place', label: '場所'},
          {key: 'date', label: '日時'},
          {key: 'num', label: '枚数', 
            formatter: value => {return (value != null)? `${value}枚`: ''}
          },
          {key: 'status', label: '状態'},
          {key: 'edit', label: '編集'},
        ],
        options: [
          {value: 'Not Applyed', text: 'Not Applyed'},
          {value: 'Applyed', text: 'Applyed'},
          {value: 'Winning', text: 'Winning'},
          {value: 'Done', text: 'Done'},
        ],
        e_options: [{text: 'Select Event', value: null },],
        members: null,
        concerts: null,
        schedules: null,
        event: {
          name: null,
        },
        event_modal_title: 'イベント追加',
        schedule: {
          concert: null,
          date: null,
          time: null,
          place: null,
        },
        edit_form: {
          date: null,
          time: null,
          place: null,
          num: 0,
          status: null,
          ticket_id: 0,
          schedule_id: 0,
        }
      }
    },
    props: ['member_id'],
    computed: {
      checkEventName(){
        return /\S/g.exec(this.event.name)? true: false
      },
      checkSchPlace(){
        return /\S/g.exec(this.schedule.place)? true: false
      },
      checkSchTime(){
        return /\S/g.exec(this.schedule.time)? true: false
      },
      checkSchDate(){
        return /\S/g.exec(this.schedule.date)? true: false
      },
      checkEditPlace(){
        return /\S/g.exec(this.edit_form.place)? true: false
      },
      checkEditTime(){
        return /\S/g.exec(this.edit_form.time)? true: false
      },
      checkEditDate(){
        return /\S/g.exec(this.edit_form.date)? true: false
      },
      checkEditState(){
        return /\S/g.exec(this.edit_form.state)? true: false
      },
      checkEditNumber(){
        return /\S/g.exec(this.schedule.number)? true: false
      }
    },
    methods: {
      selectEvt: function(concert, str){
        this.event = concert
        this.changeEvtTitle(str)
      },
      changeEvtTitle: function(str){
        this.event_modal_title = str
      },
      setObj(obj){
        /* eslint-disable */
        console.log('setObj')
        console.log(obj)
        var index = obj.date.indexOf(' ');
        console.log(obj.date.substring(0, index))
        this.edit_form.date = obj.date.substring(0, index)
        this.edit_form.time = obj.date.substring(index+1, obj.date.length)
        this.edit_form.place = obj.place
        this.edit_form.num = obj.num
        this.edit_form.status = obj.status
        this.edit_form.schedule_id = obj.schedule_id
        this.edit_form.ticket_id = obj.ticket_id
      },
      editOk(evt) {
        // Prevent modal from closing
        evt.preventDefault()
        /* eslint-disable */
        console.log(this.edit_form.date)
        if (!/\S/g.exec(this.edit_form.date)) {
          alert('Please select date')
        } else if(!/\S/g.exec(this.edit_form.time)){
          alert('Please select time')
        } else if(!/\S/g.exec(this.edit_form.place)){
          alert('Please enter place')
        } else if(!/\S/g.exec(this.edit_form.num)){
          alert('Please enter number of ticket')
        } else if(!/\S/g.exec(this.edit_form.status)){
          alert('Please select status')
        } else {
          this.saveForm()
        }
      },
      addOk(evt) {
        // Prevent modal from closing
        evt.preventDefault()
        /* eslint-disable */
        console.log(this.event)
        if (!/\S/g.exec(this.event.name)) {
          alert('Please enter your name')
        } else {
          this.submit()
        }
      },
      addSchedule(evt) {
        // Prevent modal from closing
        evt.preventDefault()
        /* eslint-disable */
        console.log(this.schedule)
        if (!/\S/g.exec(this.schedule.concert)) {
          alert('Please select event')
        } else if(!/\S/g.exec(this.schedule.date)) {
          alert('Please select date')
        } else if(!/\S/g.exec(this.schedule.time)) {
          alert('Please enter time')
        } else if(!/\S/g.exec(this.schedule.place)) {
          alert('Please enter place')
        }else{
          this.submitSchedule()
        }
      },
      getConcerts: function() {
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
              if(!this.schedules[concert.id]){
                this.schedules[concert.id] = []
              }
              this.schedules[concert.id].push({
                'edit': 'Add',
              })
            }) 
            /* eslint-disable */
            console.log('Concerts')
            console.log(this.concerts)
        })
      },
      getSchedules: function() {
        const path = this.$baseURL + `dict_schedules/` + this.member_id
        axios.get(path,
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            this.schedules = response.data
            /* eslint-disable */
            console.log('Schedules')
            console.log(this.schedules)
            this.getConcerts()
        })
      },
      submit: function(){
        const path = this.$baseURL + `regist_concert`
        axios.post(path, {'concert': this.event},
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.getSchedules()
            this.event = {name: null}
            this.$nextTick(() => {
              // Wrapped in $nextTick to ensure DOM is rendered before closing
              this.$refs.modal.hide()
            })
        })
      },
      saveForm: function(){
        let ticket = {
          id: this.edit_form.ticket_id,
          num: this.edit_form.num,
          status: this.edit_form.status,
        }
        let tmp_obj = {}
        let path = this.$baseURL + `save_ticket`
        axios.post(path, {'ticket': ticket},
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            tmp_obj = response.data
            path = this.$baseURL + `member/` + this.member_id
            axios.get(path,
              {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
              .then(response => {
                /* eslint-disable */
                console.log(response.data)
                var obj = response.data
                obj.application = tmp_obj.created
                if(tmp_obj.status == 'Winning'){
                  obj.winning = tmp_obj.modified
                }else{
                  obj.winning = null
                }
                path = this.$baseURL + `regist_member`
                /* eslint-disable */
                console.log(path)
                axios.post(path, {'member': obj},
                  {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
                  .then(response => {})
              })
        })

        let schedule = {
          id: this.edit_form.schedule_id,
          date: this.edit_form.date,
          time: this.edit_form.time,
          place: this.edit_form.place,
        }
        path = this.$baseURL + `save_schedule`
        axios.post(path, {'schedule': schedule},
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.getSchedules()
            this.$nextTick(() => {
              // Wrapped in $nextTick to ensure DOM is rendered before closing
              this.$refs.e_modal.hide()
            })
        })
      },
      submitSchedule: function(){
        const path = this.$baseURL + `regist_schedule`
        axios.post(path, {'schedule': this.schedule},
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            /* eslint-disable */
            console.log(response.data)
            this.schedule = {
              event: null,
              date: null,
              time: null,
              place: null,
            }
            this.registTicket(response.data)
            this.getSchedules()
            this.$nextTick(() => {
              // Wrapped in $nextTick to ensure DOM is rendered before closing
              this.$refs.s_modal.hide()
            })
        })
      },
      registTicket: function(schedule){
        /* eslint-disable */
        console.log('Regist Ticket')
        console.log(schedule)
        this.members.forEach((member) => {
          let num = (member.id == this.member_id)? 1: 0
          let status = (member.id == this.member_id)? 'Applyed': 'Not applyed'
          let ticket = {
            schedule: schedule,
            member: member,
            number: num,
            status: status
          } 
          const path = this.$baseURL + `regist_ticket`
          axios.post(path, {'ticket': ticket},
            {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
            .then(response => {
              /* eslint-disable */
              console.log(response.data)
          })
        })        
      },
      getMembers() {
        const path = this.$baseURL + `members`
        axios.get(path, 
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            this.members = response.data
        })
      },
      cancelEventModal(){
        event = {name: null}
        this.getConcerts()
      },
      cancelModel(){
        event = {name: null}
        this.getSchedules()
      }
    },
    mounted: function() {
      this.getSchedules()
      this.getMembers()
    }
  }
</script>

<style>
.edit-title {
  margin-left: 10px;
  float: left;
}
</style>