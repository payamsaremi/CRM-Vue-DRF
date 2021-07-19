<template>
  <div class="container">
      <div class="columns">
          <div class="column is-4 is-offset-4">
              <h1 class="title">Add member</h1>
              <form @submit.prevent="submitForm">
                  <div class="field">
                      <label>Email</label>
                      <div class="control">
                          <input type="email" name="email" class="input" v-model="username">
                      </div>
                  </div>
                  <div class="field">
                      <label>Password</label>
                      <div class="control">
                          <input type="password" name="password1" class="input" v-model="password1">
                      </div>
                  </div>
                  <div class="field">
                      <label>Repeat Password</label>
                      <div class="control">
                          <input type="password" name="password2" class="input" v-model="password2">
                      </div>
                  </div>
                  <div class="notification is-danger" v-if="errors.length">
                      <p v-for="error in errors" :key="error">{{error}}</p>
                  </div>
                  <div class="field">
                      <div class="control">
                          <button class="button is-success is-light is-rounded">Submit</button>
                      </div>
                  </div>
              </form>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
    name: 'AddMembers',
    data () {
        return {
            username: '',
            password1: '',
            password2: '',
            errors: [],
        }
    },
    methods: {
        async submitForm(){
            this.errors = []
            if(this.username === ''){
                this.errors.push('Username is missing.')
            }
            if(this.password1 === ''){
                this.errors.push('Password is missing.')
            }
            if(this.password2 === ''){
                this.errors.push('Repeat Password is missing.')
            }
            if(this.password1 !== this.password2){
                this.errors.push('Passwords are not matching')
            }

            if(!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                const formData = {
                    username: this.username,
                    password: this.password1
                }
                await axios.post('/api/v1/users/', formData)
                     .then(res => {
                         toast({
                             message: 'Member was added.',
                             type: 'is-success',
                             dismissible: true,
                             pauseOnHover: true,
                             duration: 4000,
                             position: 'bottom-right'
                         })
                    
                    const emailData = { 'email': this.username }

                    axios.post('/api/v1/teams/add_member/', emailData)
                     .then(res => {
                         this.$router.push({ 'name':'Team' })
                     })
                     .catch((err) => {
                         if(err.response) {
                             for (const property in err.response.data){
                                this.errors.push(`${property}: ${err.response.data[property]}`)
                             } 
                            // console.log(err.response.data)
                         }  else if (err.message) {
                                 toast({
                                    message: `something went wrong please check your internet connection`,
                                    type: 'is-danger',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    duration: 4000,
                                    position: 'bottom-right'
                                })
                             }
                        })
                     })
                     .catch((err) => {
                         if(err.response) {
                             for (const property in err.response.data){
                                this.errors.push(`${property}: ${err.response.data[property]}`)
                             } 
                            // console.log(err.response.data)
                         } else if (err.message) {
                                 toast({
                                    message: `something went wrong please check your internet connection`,
                                    type: 'is-danger',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    duration: 4000,
                                    position: 'bottom-right'
                                })
                             }
                     })
            }
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style>

</style>