<template>
  <div>
    <b-button variant="primary" style="float: right" v-b-modal.add-event @click="changeEvtTitle('イベント追加')"><b-badge variant="light">+</b-badge></b-button>
    <div v-for="concert in concerts" v-bind:key="concert.id">
      <div>
        <h3 style='text-align: left; margin-left: 10px; float: left'>{{concert.name}}</h3>
        <b-button class="edit-title" v-b-modal.add-event @click="selectEvt(concert, 'イベント名変更')">変更</b-button>
      </div>
      <b-table striped hover :items="schedules[concert.id]" :fields="fields">
        <template slot="edit" slot-scope="data">
          <div v-if="data.item.edit == 'Add'">
            <b-button v-b-modal.add-schedule>新規追加</b-button>
          </div>
        </template>
      </b-table>
    </div>
    <b-modal
      id="add-event"
      ref="modal"
      @ok="addOk"
      @cancel="event = {name: null}"
    >
      <div slot="modal-header">
        {{event_modal_title}}
      </div>
      <form @submit.stop.prevent="addOk">
        <label for="event-name">Name</label>
        <b-form-input id="event-name" aria-describedby="event-name-help" v-model="event.name"/>
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
            formatter: value => {return (value)? `${value}枚`: ''}
          },
          {key: 'status', label: 'ステータス'},
          {key: 'edit', label: '編集'},
        ],
        options: [
          {value: 'Applyed', text: 'Applyed'},
          {value: 'Winning', text: 'Winning'},
          {value: 'Done', text: 'Done'},
        ],
        concerts: null,
        schedules: null,
        event: {
          name: null,
        },
        event_modal_title: 'イベント追加'
      }
    },
    props: ['member_id'],
    methods: {
      selectEvt: function(concert, str){
        this.event = concert
        this.changeEvtTitle(str)
      },
      changeEvtTitle: function(str){
        this.event_modal_title = str
      },
      addOk(evt) {
        // Prevent modal from closing
        evt.preventDefault()
        /* eslint-disable */
        console.log(this.event)
        if (!this.event.name) {
          alert('Please enter your name')
        } else {
          this.submit()
        }
      },
      getConcerts: function() {
        const path = this.$baseURL + `concerts`
        axios.get(path,
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            this.concerts = response.data
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
            for(let i in this.schedules) {
                this.schedules[i].push({
                  'edit': 'Add',
                })
            }
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
    },
    mounted: function() {
      this.getSchedules()
    }
  }

</script>

<style>
.edit-title {
  margin-left: 10px;
  float: left;
}
</style>