<template>
  <div>
    <div v-for="concert in concerts" v-bind:key="concert.id">
      <h3 style='text-align: left; margin-left: 10px'>{{concert.name}}</h3>
      <b-table striped hover :items="schedules[concert.id]" :fields="fields">
      </b-table>
    </div>
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
            formatter: value => {return `${value}枚`}
          },
          {key: 'status', label: 'ステータス'},
        ],
        concerts: null,
        schedules: null,
      }
    },
    props: ['member_id'],
    methods: {
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
            /* eslint-disable */
            console.log('Schedules')
            console.log(this.schedules)
            this.getConcerts()
        })
      },
    },
    mounted: function() {
      this.getSchedules()
    }
  }

</script>
