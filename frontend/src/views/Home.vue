<template>
  <div class="home">
    <Event/>
  </div>
</template>

<script>
// @ is an alias to /src
import Event from '@/components/Event.vue'

export default {
  name: 'home',
  components: {
    Event
  }
}
</script>
