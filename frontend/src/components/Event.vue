<template>
  <div>
    <b-table striped hover :items="items" :fields="fields"></b-table>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
    data() {
      return {
        fields: ['イベント', '詳細'],
        items: [
          {name: '十五祭'}, 
        ]
      }
    }
  }
</script>

<style>
</style>