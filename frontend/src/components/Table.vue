<template>
  <div>
    <b-table striped hover :items="members" :fields="fields">
      <template slot="name" slot-scope="data">
        <router-link v-bind:to="{ name : 'manage', params : { id: data.item.id }}">{{ data.value }}</router-link>
      </template>
      <template slot="winning" slot-scope="data">
        <b-form-input :type="`date`" v-model="data.winning"></b-form-input>
      </template>
    </b-table>
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
          {key: 'winning', label: '当選日'}],
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
        })
      },
    },
    created: function() {
      this.getMembers()
    }
  }
</script>
