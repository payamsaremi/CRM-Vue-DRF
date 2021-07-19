import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      username: ''
    },
    team: {
      id: 0,
      name: ''
    }
  },
  mutations: {
    initializeStore(state) {
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        //User info
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('userid')
        //Team info
        state.team.name = localStorage.getItem('team_name')
        state.team.id = localStorage.getItem('team_id')

      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.username = ''
        state.user.id = 0
        state.team.name = ''
        state.team.id = 0
      }
    },
    setIsLoading(state, status){
      state.isLoading = status
    },
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user){
      state.user = user
    },
    setTeam(state, team){
      state.team = team
      localStorage.setItem('team_id', team.id)
      localStorage.setItem('team_name', team.name)
    }
  },
  actions: {
  },
  modules: {
  }
})
