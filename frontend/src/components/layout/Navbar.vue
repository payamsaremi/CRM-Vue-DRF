<template>
  <nav class="navbar is-white">
      <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
            <strong>
                <svg width="50" height="50" viewBox="-50 -50 100 100">
                    <circle r="40" fill="#D1459B" />
          </svg>
            </strong>
          </router-link>
          <a role="button" ref="burgerButton" @click="toggleBurgerMenu" class="navbar-burger" :class="{ 'is-active':isActive }" aria-label="menu" aria-expanded="false" data-target="navbarMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            </a>
      </div>
      <div id="navbarMenu" class="navbar-menu" :class="{ 'is-active':isActive }">
          <div class="navbar-end">
              <div class="navbar-item">
                  <div class="buttons">
                      <template v-if="$store.state.isAuthenticated">
                        <router-link @click="isActive = false" class="button is-link is-light is-rounded" to="/dashboard/team">Team</router-link>
                        <router-link @click="isActive = false" class="button is-link is-light is-rounded" to="/dashboard/leads">Lead</router-link>
                        <router-link @click="isActive = false" class="button is-link is-light is-rounded" to="/dashboard/my-account">My account</router-link>
                      </template>
                      <template v-if="!$store.state.isAuthenticated">
                        <router-link @click="isActive = false" class="button is-success is-light is-rounded" to="/sign-up">Sign up</router-link>
                        <router-link @click="isActive = false" class="button is-success is-light is-rounded" to="/log-in">Log in</router-link>
                      </template>
                  </div>
              </div>
          </div>
      </div>
  </nav>
</template>

<script>
export default {
    name: 'Navbar',
    data(){
        return {
            isActive: false
        }
    },
    methods: {
        toggleBurgerMenu(){
            this.isActive = !this.isActive
        }
    }
}
</script>

<style>

</style>