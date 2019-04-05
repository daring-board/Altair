<template>
  <div>
    <b-table striped hover :items="members" :fields="fields">
      <template slot="name" slot-scope="data">
        <router-link v-bind:to="{ name : 'manage', params : { id: data.item.id }}">{{ data.value }}</router-link>
      </template>
      <template slot="edit" slot-scope="data">
        <div v-if="data.item.edit == 'Add'">
          <b-button v-b-modal.add-modal>新規追加</b-button>
        </div>
        <div v-else>
          <b-button v-b-modal.edit-modal>変更</b-button>
        </div>
      </template>
    </b-table>
    <b-modal id="add-modal" ref="add-ref" hide-footer>
      <NewMember v-on:new-member-add="getMembers"/>
    </b-modal>
    <b-modal id="edit-modal">
      <NewMember member=data.value v-on:new-member="getMembers" hide-footer/>
    </b-modal>
  </div>
</template>

<script>
  import axios from 'axios'
  import NewMember from '@/components/NewMember.vue'

  export default {
    components: {
      NewMember
    },
    data() {
      return {
        // Note `isActive` is left out and will not appear in the rendered table
        fields: [
          {key: 'name', label: '名前'},
          {key: 'application', label: '申し込み日'},
          {key: 'winning', label: '当選日'},
          {key: 'edit', label: '編集'}],
        members: []
      }
    },
    methods: {
      getMembers() {
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
      addMembers() {
        /* eslint-disable */
        console.log(response.data)
        this.$refs['add-ref'].hide()
        this.getMembers()
      }
    },
    created: function() {
      this.getMembers()
    }
  }
</script>
