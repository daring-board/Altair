<template>
  <div>
    <b-table striped hover :items="items" :fields="fields">
      <template slot="event" slot-scope="row">
        <router-link class="nav-link" to="/">{{row.item.event}}</router-link>
      </template>
      <template slot="detail" slot-scope="row">
        <b-button @click="row.toggleDetails">
          <i class="fas fa-caret-down"></i>
        </b-button>
      </template>
      <template slot="row-details" slot-scope="row">
        <b-card>
          <b-row class="mb-2">
            <b>{{row.item.n_member}}名義申し込み中: {{row.item.n_win}}当選</b>
          </b-row>
          <b-row class="mb-2">
            <b-col>
              <b-button v-b-modal.add-modal @click="selectMember(row.item, '編集')">
                <i class="fas fa-edit"></i>
              </b-button>
            </b-col>
            <b-col>
              <b-button v-b-modal.confirm-modal @click="selectMember(row.item, '削除')">
                <i class="fas fa-trash"></i>
              </b-button>
              <!-- The modal -->
              <b-modal 
                id="confirm-modal"
                @ok="deleteMember"
              >
                Are you sure?
              </b-modal>
            </b-col>
          </b-row>
        </b-card>
      </template>
    </b-table>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
    data() {
      return {
        fields: {'event': 'イベント', 'detail': '詳細'},
        items: [
          {'event': '十五祭', 'n_member': 3, 'n_win': 0}, 
        ]
      }
    }
  }
</script>

<style>
</style>