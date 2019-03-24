<template>
  <div>
    <b-table striped hover :items="members" :fields="fields">
      <template slot="name" slot-scope="data">
        <a :href="`/manage`">{{ data.value }}</a>
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
        const path = `http://localhost:5000/api/members`
        axios.get(path)
          .then(response => {
            this.members = response.data
            /* eslint-disable */
            console.log(this.members)
        })
      },
    },
    created: function() {
      this.getMembers()
    }
  }
</script>
