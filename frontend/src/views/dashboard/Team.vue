<template>
  <div class="container">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">{{ team.name }}</h1>
              <div v-if="team.created_by.id === parseInt($store.state.user.id)">
              <router-link class="button is-link is-small is-outlined" :to="{ 'name': 'AddMembers' }">Add member</router-link>
              </div>
          </div>
          

          <div class="column is-12">
              <h2 class="subtitle">Members</h2>
              <table class="table is-fullwidth">
                  <thead>
                      <tr>
                          <th>Name</th>
                          <th>status</th>
                      </tr>
                  </thead>
                  <tbody>
                      <tr v-for="member in team.members" :key="member.id">
                          <td>
                              {{ member.username }}
                          </td>
                          <td>
                              <span v-if="member.id === parseInt($store.state.user.id)" class="tag is-info is-light ">
                                  Manager
                              </span>
                          </td>
                      </tr>
                  </tbody>
              </table>
          </div>

      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Team',
    data(){
        return {
           team: {
                members: [],
                created_by: {}
           }
        }
    },
    mounted(){
        this.getTeam()
    },
    methods: {
        async getTeam(){
            this.$store.commit('setIsLoading', true)
            await axios.get('/api/v1/teams/get_my_team/')
                
                           .then( res => {
                               console.log(res.data)
                               this.team = res.data
                            })
                           .catch( err => {
                                console.log(err)
                            })

                this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style>

</style>