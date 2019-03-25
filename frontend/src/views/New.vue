<template>
  <div class="new">
    <b-container>
      <br/>
      <NewMember/>
      <br/>
      <NewEvent/>
    </b-container>
  </div>
</template>

<script>
import NewMember from '@/components/NewMember.vue'
import NewEvent from '@/components/NewEvent.vue'

export default {
  name: 'new',
  components: {
    NewMember,
    NewEvent
  }
}
</script>
