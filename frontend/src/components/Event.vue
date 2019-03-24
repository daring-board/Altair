<template>
  <div>
    <h3 style='text-align: left; margin-left: 10px'>コンサート</h3>
    <b-table striped hover :items="items" :fields="fields">
    </b-table>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        // Note `isActive` is left out and will not appear in the rendered table
        fields: [
          {key: 'ID', label: 'No'},
          {key: 'date', label: '日時'},
          {key: 'num', label: '枚数', 
            formatter: value => {return `${value}枚`}
          },
          {key: 'status', label: 'ステータス'},
          ],
        items: [
          {ID: 1, date: 'yyyy.mm.dd.hh:mm', num: 1, status: '申込済' },
        ],
      }
    }
  }

</script>
