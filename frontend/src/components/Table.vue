<template>
  <div>
    <b-table striped hover :items="members" :fields="fields">
      <template slot="name" slot-scope="data">
        <router-link v-bind:to="{ name : 'manage', params : { id: data.item.id }}">{{ data.value }}</router-link>
      </template>
      <template slot="edit" slot-scope="data">
        <div v-if="data.item.edit == 'Add'">
          <b-button v-b-modal.add-modal @click="changeTitle('新規追加')">
            <i class="fas fa-plus"></i>
          </b-button>
        </div>
        <div v-else>
          <b-button v-b-modal.add-modal @click="selectMember(data.item, '変更')">
            <i class="fas fa-edit"></i>
          </b-button>
        </div>
      </template>
    </b-table>
    <b-modal
      id="add-modal"
      ref="modal"
      @ok="addOk"
      @hide="cancel"
    >
      <div slot="modal-header">
        {{title_str}}
      </div>
      <form @submit.stop.prevent="submit">
        <label for="member-name">Name</label>
        <b-form-input id="member-name" 
          aria-describedby="member-name-help"
          required
          v-model="member['name']"
          :state="checkName"
        />
        <b-form-text id="member-name-help">
          Input name of new member, and push following button. 
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
          {key: 'name', label: '名前'},
          {key: 'application', label: '申し込み日'},
          {key: 'winning', label: '当選日'},
          {key: 'edit', label: '編集'}],
        members: [],
        member: {
          'name': '',
          'application': '',
          'winning': '',
          'edit': '',
        },
        title_str: '新規追加'
      }
    },
    computed: {
      checkName(){
        if(this.member['name'].length > 50){
          return false
        }
        return /\S/g.exec(this.member['name'])? true: false
      },
    },
    methods: {
      changeTitle(str){
        this.title_str = str
      },
      selectMember(data, title){
        this.changeTitle(title)
        /* eslint-disable */
        console.log(data)
        this.member = data
      },
      getMembers() {
        /* eslint-disable */
        console.log('getMember')
        const path = this.$baseURL + `members`
        axios.get(path, 
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            this.members = response.data
            this.members.push({
              'name': '',
              'application': '',
              'winning': '',
              'edit': 'Add',
            })
        })
      },
      cancel() {
        this.getMembers()
      },
      addOk(evt) {
      // Prevent modal from closing
        evt.preventDefault()
        /* eslint-disable */
        console.log(this.member)
        if (!/\S/g.exec(this.member['name'])) {
          alert('Please enter your name')
        } if(this.member['name'].length > 50){
          alert('場所名が長すぎます。50字以内にして下さい！！')
        } else {
          this.submit()
        }
      },
      clearName(){
        this.member = {
          'name': '',
          'application': '',
          'winning': '',
          'edit': '',
        }
      },
      submit() {
        const path = this.$baseURL + `regist_member`
        axios.post(path, {'member': this.member}, 
          {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
          .then(response => {
            this.getMembers()
            this.$nextTick(() => {
              // Wrapped in $nextTick to ensure DOM is rendered before closing
              this.$refs.modal.hide()
            })
            /* eslint-disable */
            console.log(response.data)
        })
      }
    },
    created: function() {
      this.getMembers()
    }
  }
</script>
