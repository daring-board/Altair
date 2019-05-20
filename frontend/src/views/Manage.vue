<template>
  <div class="manage">
    <Names :concert_id="id"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Names from '@/components/Names.vue'

export default {
  name: 'manage',
  components: {
    Names
  },
  props: ['id'],
}
</script>
