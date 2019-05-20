<template>
  <div>
    <b-table striped hover :items="items" :fields="fields">
      <template slot="name" slot-scope="row">
        <router-link class="nav-link" :to="{name: 'manage', params: { id: row.item.id }}">{{row.item.name}}</router-link>
      </template>
      <template slot="detail" slot-scope="row">
        <div v-if="row.item.detail == 'Add'">
          <b-button v-b-modal.add-modal @click="setModalAttribute('new', null)">
            <i class="fas fa-plus"></i>
          </b-button>
        </div>
        <div v-else>
          <b-button @click="row.toggleDetails">
            <i class="fas fa-caret-down"></i>
          </b-button>
        </div>
      </template>
      <template slot="row-details" slot-scope="row">
        <b-card>
          <b-row class="mb-2">
            <b>{{row.item.n_member}}名義申し込み中: {{row.item.n_win}}当選</b>
          </b-row>
          <b-row class="mb-2">
            <b-col>
              <b-button v-b-modal.add-modal @click="setModalAttribute('edit', row.item)">編集</b-button>
            </b-col>
            <b-col>
              <b-button v-b-modal.confirm-modal @click="event=row.item">削除</b-button>
            </b-col>
          </b-row>
        </b-card>
      </template>
    </b-table>
    <!-- The modal -->
    <b-modal 
      id="confirm-modal"
      @ok="delConcert(event.id)"
      @cancel="initNewEvent()"
    >
      {{event.name}}を削除しますか？
    </b-modal>
    <b-modal
      id="add-modal"
      ref="modal"
      :ok-disabled="!validation"
      @ok="addOk"
      @cancel="initNewEvent()"
    >
      <div slot="modal-header">
        {{modal_label.header}}
      </div>
      <form @submit.stop.prevent="addOk">
        <label for="event-name">イベント名</label>
        <b-form-input
          id="event-name" 
          aria-describedby="event-name-help"
          v-model="event.name"
          :state="validation"
          required
        />
        <b-form-text id="event-name-help">
          {{modal_label.help}}
        </b-form-text>
        <b-form-invalid-feedback :state="validation"></b-form-invalid-feedback>
        <b-form-valid-feedback :state="validation"></b-form-valid-feedback>
      </form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      fields: {'name': 'イベント', 'detail': '詳細'},
      items: [],
      event: {},
      modal_label: {}
    }
  },
  created: function(){
    this.getConcerts()
    this.initNewEvent()
    this.setModalAttribute('new', null)
  },
  computed: {
    validation(){
      return this.checkName()
    }
  },
  methods: {
    checkName(){
      if(this.event.name.length > 50){
        return false
      }
      return /\S/g.exec(this.event.name)? true: false
    },
    getConcerts(){
      const path = this.$baseURL + `concerts`
      axios.get(path, {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
        .then(response => {
          this.items = response.data
          this.items.push({
            'name': '',
            'detail': 'Add',
          })
          /* eslint-disable */
          console.log(this.items)
        })
    },
    delConcert(concert_id){
      const path = this.$baseURL + `del_concert/` + concert_id
      axios.get(path, {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
        .then(response => {
          /* eslint-disable */
          console.log(response.data)
          this.getConcerts()
          this.initNewEvent()
        })
    },
    addOk(evt){
      if(!this.checkName()){
        return
      }
      // Prevent modal from closing
      evt.preventDefault()
      const path = this.$baseURL + `regist_concert`
      /* eslint-disable */
      console.log(this.event)    
      axios.post(path, {'concert': this.event},
        {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
        .then(response => {
          /* eslint-disable */
          console.log(response.data)
          this.initNewEvent()
          this.getConcerts()
          this.$nextTick(() => {
            // Wrapped in $nextTick to ensure DOM is rendered before closing
            this.$refs.modal.hide()
          })
      })
    },
    initNewEvent(){
      this.event = {name: ''}
    },
    setModalAttribute(attr, item){
      if(attr == 'edit'){
        this.modal_label = {
          header: 'イベント変更',
          help: 'イベント名を入力してください'
        }
        /* eslint-disable */
        console.log(item)
        this.event = item
      }else{
        this.modal_label = {
          header: 'イベント追加',
          help: '新しいイベント名を入力してください'
        }
      }
    }
  }
}
</script>

<style>
</style>