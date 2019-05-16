<template>
  <div class="manage">
    <h2 style="margin-top: 10px">{{ concert.name }}</h2>
    <Names/>
  </div>
</template>

<script>
// @ is an alias to /src
import Names from '@/components/Names.vue'
import axios from 'axios'

export default {
  name: 'manage',
  components: {
    Names
  },
  data: function() {
    return {
      concert: {'name': ''},
    }
  },
  props: ['id'],
  mounted: function() {
    const path = this.$baseURL + `concert/` + this.id
    axios.get(path,
      {headers: {'Authorization': 'JWT ' + this.$store.state.accessToken}})
      .then(response => {
        this.concert = response.data
        /* eslint-disable */
        console.log(this.concert)
    })
  }
}
</script>
