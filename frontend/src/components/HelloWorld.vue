<template>
  <div class="hello">
    <p>{{ msg }}</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button class= "btn btn-primary" @click="getRandom">New random number</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
    },
    created () {
      this.getRandom()
    }
  }
}
</script>
