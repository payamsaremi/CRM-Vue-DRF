<template>
  <div class="container">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">Add team</h1>
          </div>
      </div>
      <div class="column is-12">
          <form @submit.prevent="submitForm">
              <div class="field">
                  <label class="label">Team name</label>
                  <input class="input" name="team_name" type="text" v-model="name">
              </div>
              <div class="field">
                  <button class="button is-success is-rounded">Submit</button>
              </div>
          </form>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'AddTeam',
    data(){
        return {
            name: ''
        }
    },
    methods: {
        async submitForm(){
            this.$store.commit('setIsLoading', true)

            const team = {
                name: this.name
            }
            await axios.post('/api/v1/teams/', team)
                       .then( res => {
                           console.log(res)
                    toast({
                            message: 'Team added successfully',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 4000,
                            position: 'bottom-right'
                            })
                    this.$store.commit('setTeam', { 'id': res.data.id, 'name': this.name})
                    this.$router.push('/dashboard/leads')
                            })
                            .catch (err => {
                                console.log(err)
                            })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style>

</style>