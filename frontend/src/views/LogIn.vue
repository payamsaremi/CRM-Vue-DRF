<template>
  <div class="container">
      <div class="columns">
          <div class="column is-4 is-offset-4">
              <h1 class="title">Log in</h1>
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
                          <input type="password" name="password" class="input" v-model="password">
                      </div>
                  </div>
                  <div class="notification is-danger" v-if="errors.length">
                      <p v-for="error in errors" :key="error">{{error}}</p>
                  </div>
                  <div class="field">
                      <div class="control">
                          <button class="button is-link is-light is-rounded">Submit</button>
                      </div>
                  </div>
              </form>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data(){
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        async submitForm(){
            
            this.errors = []
            if(this.username === ''){
                this.errors.push('What is your username?')
            }
            if(this.password === ''){
                this.errors.push('Password field is empty.')
            }

            if(!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }

                await axios.post('/api/v1/token/login', formData)
                    .then( res => {
                        const token = res.data.auth_token
                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] =  'Token ' + token
                        localStorage.setItem('token', token)

                    })
                    .catch( err => {
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
                await axios.get('/api/v1/users/me')
                    .then( res => {
                        this.$store.commit('setUser', {
                            'id': res.data.id,
                            'username': res.data.username
                        })
                        localStorage.setItem('username', res.data.username)
                        localStorage.setItem('userid', res.data.id)
                        console.log(res)
                    })
                    .catch( err => {
                        console.log(err)
                    })
                  
                
                await axios.get('/api/v1/teams/get_my_team/')
                           .then( res => {
                               this.$store.commit('setTeam', { 
                                   'id': res.data.id,
                                   'name': res.data.name
                            })

                            if(!this.$store.state.team.id){
                                this.$router.push('/dashboard/add-team')
                                console.log('no team')
                                } else {
                                this.$router.push('/dashboard/my-account')
                                console.log(this.$store.state.team)
                                }
                            })
                           .catch( err => {
                                console.log(err)
                            })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
}
</script>

<style>

</style>