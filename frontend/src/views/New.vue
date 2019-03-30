<template>
  <div class="new">
    <b-container>
      <br/>
      <NewMember/>
      <br/>
      <NewEvent/>
      <br/>
      <NewSchedule/>
      <br/>
      <NewTicket/>
    </b-container>
  </div>
</template>

<script>
import NewMember from '@/components/NewMember.vue'
import NewEvent from '@/components/NewEvent.vue'
import NewSchedule from '@/components/NewSchedule.vue'
import NewTicket from '@/components/NewTicket.vue'

export default {
  name: 'new',
  components: {
    NewMember,
    NewEvent,
    NewTicket,
    NewSchedule
  },
}
</script>
