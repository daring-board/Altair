<template>
  <div class="new">
    <div v-if="flag">
      <b-alert variant="success" show>{{message}}</b-alert>
    </div>
    <b-container>
      <br/>
      <NewMember @success="on_success"/>
      <br/>
      <NewEvent @success="on_success"/>
      <br/>
      <NewTicket @success="on_success"/>
    </b-container>
  </div>
</template>

<script>
import NewMember from '@/components/NewMember.vue'
import NewEvent from '@/components/NewEvent.vue'
import NewTicket from '@/components/NewTicket.vue'

export default {
  name: 'new',
  components: {
    NewMember,
    NewEvent,
    NewTicket
  },
  data: function() {
    return {
      flag: false,
      message: ''
    }
  },
  methods: {
    on_success(message){
      this.flag = true
      this.message = message

    }
  }
}
</script>
