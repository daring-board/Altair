<template>
  <div>
    <h2 style="margin-top: 10px">{{ concert.name }}</h2>
    <b-table striped hover :items="items" :fields="fields">
      <template slot="name" slot-scope="row">
        <router-link class="nav-link" :to="{}">{{row.item.name}}</router-link>
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
            <b-col>
              申込日
            </b-col>
            <b-col>
              当選日
            </b-col>
          </b-row>
          <b-row class="mb-2">
            <b-col>
              {{row.item.infos[0]['datetime']}}
            </b-col>
            <b-col>
              {{row.item.infos[0]['datetime']}}
            </b-col>
          </b-row>
          <b-row class="mb-2">
            <b-col>
              <b-button v-b-modal.add-modal @click="setModalAttribute('edit', row.item)">編集</b-button>
            </b-col>
            <b-col>
              <b-button v-b-modal.confirm-modal @click="member=row.item">削除</b-button>
            </b-col>
          </b-row>
        </b-card>
      </template>
    </b-table>
    <!-- The modal -->
    <b-modal 
      id="confirm-modal"
      @ok="delMember(member.id)"
      @cancel="initNewMember()"
    >
      {{member.name}}を削除しますか？
    </b-modal>
    <b-modal
      id="add-modal"
      ref="modal"
      :ok-disabled="!validation"
      @ok="addOk"
      @cancel="initNewMember()"
    >
      <div slot="modal-header">
        {{modal_label.header}}
      </div>

      <form @submit.stop.prevent="addOk" style="align: left">
        <label for="apply-name">名義人</label>
        <b-form-input
          id="apply-name" 
          aria-describedby="apply-name-help"
          v-model="member.name"
          :state="validation"
          required
        />
        <b-form-text id="apply-name-help">
          {{modal_label.name_help}}
        </b-form-text>
        <b-form-invalid-feedback :state="validation"></b-form-invalid-feedback>
        <b-form-valid-feedback :state="validation"></b-form-valid-feedback>

        <label for="date">Date</label>
        <b-form-input
          class="text-center"
          id="date"
          :type="`date`"
          aria-describedby="date-help"
          required
        />
        <b-form-text id="date-help">
          {{modal_label.date_help}}
        </b-form-text>

        <label for="time">Time</label>
        <b-form-input
          class="text-center"
          id="time"
          :type="`time`"
          aria-describedby="time-help"
          required
        />
        <b-form-text id="time-help">
          {{modal_label.time_help}}
        </b-form-text>

        <label for="place">会場</label>
        <b-input
          id="place"
          aria-describedby="place-help"
          required
        />
        <b-form-text id="place-help">
          {{modal_label.place_help}}
        </b-form-text>

        <label for="num">枚数</label>
        <b-form-input
          class="text-center"
          id="num"
          :type="`number`"
          aria-describedby="num-help"
          required
        />
        <b-form-text id="num-help">
          {{modal_label.num_help}}
        </b-form-text>

        <label for="remark">備考</label>
        <b-form-textarea
          id="remark"
          aria-describedby="remark-help"
        />
        <b-form-text id="remark-help">
          {{modal_label.remark_help}} 
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
      fields: {'name': '名前', 'detail': '詳細'},
      items: [],
      member: {},
      modal_label: {},
      concert: {}
    }
  },
  props: ['concert_id'],
  created: function(){
    this.initNewMember()
    this.setModalAttribute('new', null)
    this.getConcert()
  },
  computed: {
    validation(){
      return this.checkName()
    }
  },
  methods: {
    checkName(){
      if(this.member.name.length > 50){
        return false
      }
      return /\S/g.exec(this.member.name)? true: false
    },
    getConcert(){
      const path = this.$baseURL + `concert/` + this.concert_id
      axios.get(path,
        {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
        .then(response => {
          this.concert = response.data
          /* eslint-disable */
          console.log(this.concert)
          this.getTickets()
      })
    },
    getTickets(){
      const path = this.$baseURL + `tickets/` + this.concert.id
      axios.get(path, {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
        .then(response => {
          this.items = response.data
          /* eslint-disable */
          console.log(response.data)
          this.items.push({
            'name': '',
            'detail': 'Add',
          })
          /* eslint-disable */
          console.log(this.items)
        })
    },
    delMember(member_id){
      const path = this.$baseURL + `del_member/` + member_id
      axios.get(path, {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
        .then(response => {
          /* eslint-disable */
          console.log(response.data)
          this.getMembers()
          this.initNewMember()
        })
    },
    addOk(evt){
      if(!this.checkName()){
        return
      }
      // Prevent modal from closing
      evt.preventDefault()
      const path = this.$baseURL + `regist_member`
      /* eslint-disable */
      console.log(this.member)    
      axios.post(path, {'concert': this.member},
        {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
        .then(response => {
          /* eslint-disable */
          console.log(response.data)
          this.initNewMember()
          this.getMembers()
          this.$nextTick(() => {
            // Wrapped in $nextTick to ensure DOM is rendered before closing
            this.$refs.modal.hide()
          })
      })
    },
    initNewMember(){
      this.member = {name: ''}
    },
    setModalAttribute(attr, item){
      if(attr == 'edit'){
        this.modal_label = {
          header: '申込情報変更',
          name_help: '',
          date_help: '',
          time_help: '',
          place_help: '',
          num_help: '',
          remark_help: '備考の入力はオプションです'
      }
        /* eslint-disable */
        console.log(item)
        this.member = item
      }else{
        this.modal_label = {
          header: '申込追加',
          name_help: '',
          date_help: '',
          time_help: '', 
          place_help: '',
          num_help: '',
          remark_help: '備考の入力はオプションです'
        }
      }
    }
  }
}
</script>

<style>
</style>