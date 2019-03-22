<template>
  <div class="calender">
      <div id="calendar-nav">
          <i class="glyphicon glyphicon-menu-left" v-on:click="moveLastMonth"></i>
          <span>{{calData.year}} - {{getMonthName(calData.month)}}</span>
          <i class="glyphicon glyphicon-menu-right"  v-on:click="moveNextMonth"></i>
      </div>
      <table id="calendar" class="table table-bordered">
          <thead>
              <tr>
                  <th v-for="week in weeks" :key="week.id">{{week}}</th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="week in calendar" :key="week.id">
                  <td v-for="day in week" :key="day.id">{{day.day}}</td>
              </tr>
          </tbody>
      </table>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/vue/0.12.8/vue.min.js"></script>
<script>
import datepicker from 'vuejs-datepicker'

export default {
  components: {
    datepicker
  },
  data: function(){
    return {
      weeks: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      calData: {year: 0, month: 0}
    }
  },
  created: function (){
      var date = new Date();
      this.calData.year = date.getFullYear();
      this.calData.month = date.getMonth() + 1;
  },
  methods: {
      getMonthName: function(month) {
          var monthName = ['January','February','March','April','May','June','July','August','September','October','November','December'];
          return monthName[month - 1];
      },
      moveLastMonth: function() {
          if (this.calData.month == 1) {
              this.calData.year--;
              this.calData.month = 12;
          }
          else {
              this.calData.month--;
          }
      },
      moveNextMonth: function() {
          if (this.calData.month == 12) {
              this.calData.year++;
              this.calData.month = 1;
          }
          else {
              this.calData.month++;
          }
      }
  },
  computed: {
      calendar: function () {
          // 1日の曜日
          var firstDay = new Date(this.calData.year, this.calData.month - 1, 1).getDay();
          // 晦日の日にち
          var lastDate = new Date(this.calData.year, this.calData.month, 0).getDate();
          // 日にちのカウント
          var dayIdx = 1;

          var calendar = [];
          for (var w = 0; w < 6; w++) {
              var week = [];

              // 空白行をなくすため
              if (lastDate < dayIdx) {break;}

              for (var d = 0; d < 7; d++) {
                  if (w == 0 && d < firstDay) {
                      week[d] = {day: ''};
                  } else if (w == 6 && lastDate < dayIdx) {
                      week[d] = {day: ''};
                      dayIdx++;
                  } else if (lastDate < dayIdx) {
                      week[d] = {day: ''};
                      dayIdx++;
                  } else {
                      week[d] = {day: dayIdx};
                      dayIdx++;
                  }
              }

              calendar.push(week);
          }
          return calendar;
      }
  }
}
</script>

<style>
/* カレンダーナビのスタイル */
#calendar-nav {
    text-align: center;
}

#calendar-nav span {
    display: inline-block;
    width: 200px;
}

#calendar-nav i:hover {
    cursor: pointer;
}

/* カレンダーのスタイル */
.table th, td{
    text-align: center;
}

#calendar th:first-child {
    background-color: #FEEEFF;
}
#calendar td:first-child {
    background-color: #FEEEFF;
}
#calendar th:nth-child(7) {
    background-color: #DFFFFF
}
#calendar td:nth-child(7) {
    background-color: #DFFFFF
}

#calendar td:hover {
    opacity: 0.6;
}
</style>