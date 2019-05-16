<template>
  <div>
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
              <b-button v-b-modal.add-modal @click="setModalAttribute('edit', row.item)">編集</b-button>
            </b-col>
            <b-col>
              <b-button v-b-modal.confirm-modal>削除</b-button>
              <!-- The modal -->
              <b-modal 
                id="confirm-modal"
                @ok="delConcert(row.item.id)"
              >
                {{row.item.name}}を削除しますか？
              </b-modal>
            </b-col>
          </b-row>
        </b-card>
      </template>
    </b-table>
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
        <label for="apply-name">名義</label>
        <b-form-input
          id="apply-name" 
          aria-describedby="apply-name-help"
          v-model="member.name"
          :state="validation"
          required
        />
        <b-form-text id="apply-name-help">
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
      fields: {'name': '名前', 'detail': '詳細'},
      items: [],
      member: {},
      modal_label: {}
    }
  },
  created: function(){
    this.getMembers()
    this.initNewMember()
    this.setModalAttribute('new', null)
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
    getMembers(){
      const path = this.$baseURL + `members`
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
    delMember(member_id){
      const path = this.$baseURL + `del_concert/` + member_id
      axios.get(path, {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
        .then(response => {
          /* eslint-disable */
          console.log(response.data)
          this.getMembers()
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
          help: '申込情報入力してください'
        }
        /* eslint-disable */
        console.log(item)
        this.member = item
      }else{
        this.modal_label = {
          header: '申込追加',
          help: '申込を行う名義を入力してください'
        }
      }
    }
  }
}
</script>

<style>
</style>