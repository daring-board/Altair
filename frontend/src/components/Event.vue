<template>
  <div>
    <div v-for="concert in concerts" v-bind:key="concert.id">
      <h3 style='text-align: left; margin-left: 10px'>{{concert.name}}</h3>
      <b-table striped hover :items="tickets[concert.id]" :fields="fields">
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
          {key: 'ID', label: 'No'},
          {key: 'date', label: '日時'},
          {key: 'num', label: '枚数', 
            formatter: value => {return `${value}枚`}
          },
          {key: 'status', label: 'ステータス'},
        ],
        concerts: null,
        tickets: null
      }
    },
    props: ['member_id'],
    methods: {
      getConcerts: function() {
        const path = this.$baseURL + `concerts`
        axios.get(path)
          .then(response => {
            this.concerts = response.data
            /* eslint-disable */
            console.log('Concerts')
            console.log(this.concerts)
        })
      },
      getTickets: function() {
        console.log(this.member_id)
        const path = this.$baseURL + `ticket/` + this.member_id
        axios.get(path)
          .then(response => {
            this.tickets = response.data
            /* eslint-disable */
            console.log('Tickets')
            console.log(this.tickets)

            this.getConcerts()
        })
      }
    },
    created: function() {
      this.getTickets()
    }
  }

</script>
