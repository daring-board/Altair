<template>
  <div>
    <b-table striped hover :items="items" :fields="fields" />
    <p>Random number from backend: {{ randomNumber }}</p>
    <button class= "btn btn-primary" @click="getRandom">New random number</button>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        // Note `isActive` is left out and will not appear in the rendered table
        fields: ['first_name', 'last_name', 'age'],
        items: [
          { isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney' }
        ],
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
