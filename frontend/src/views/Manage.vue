<template>
  <div class="manage">
    <h2 style="margin-top: 10px">{{ member.name }}</h2>
    <Event :member_id='id'/>
  </div>
</template>

<script>
// @ is an alias to /src
import Event from '@/components/Event.vue'
import axios from 'axios'

export default {
  name: 'manage',
  components: {
    Event
  },
  data: function() {
    return {
      member: {'name': 'No name'},
    }
  },
  props: ['id'],
  mounted: function() {
    const path = this.$baseURL + `member/` + this.id
    axios.get(path)
      .then(response => {
        this.member = response.data
        /* eslint-disable */
        console.log(this.member)
    })
  }
}
</script>
