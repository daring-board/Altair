<template>
  <div class="manage">
    <h2>Dickerson</h2>
    <Event/>
  </div>
</template>

<script>
// @ is an alias to /src
import Event from '@/components/Event.vue'

export default {
  name: 'manage',
  components: {
    Event
  }
}
</script>
