<template>
  <div>
    <Navbar />
    <div :class="{'loading': $store.state.isLoading}" ></div>
    <!-- <div class="is-loading-bar has-text-centered" :class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div> -->
    <section class="section" >
      <router-view />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/layout/Navbar.vue'
export default {
  name: 'App',
  components: {
    Navbar,
  },
  beforeCreate(){
    this.$store.commit('initializeStore')

    console.log(this.$store.state.user)
    console.log(this.$store.state.team)

    if(this.$store.state.token){
      axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }

  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

/* Absolute Center Spinner */
.loading {
  position: fixed;
  z-index: 999;
  width: 80px;
  height: 80px;
  overflow: show;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

/* Transparent Overlay */
.loading:before {
  content: '';
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
    background: radial-gradient(rgba(255, 255, 255, 0.8), rgb(255, 255, 255));
  background: -webkit-radial-gradient(rgba(255, 255, 255, 0.8), rgb(255, 255, 255));
}

/* :not(:required) hides these rules from IE9 and below */
.loading:not(:required) {
  /* hide "loading..." text */
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}


.loading:not(:required):after {
  content: ' ';
  display: block;
  width: 70px;
  height: 70px;
  margin: auto;
  border-radius: 50%;
  border: 6px solid rebeccapurple;
  border-color: #ccc transparent #ccc transparent;
  -webkit-animation: lds-dual-ring 1.2s linear infinite;
  -moz-animation: lds-dual-ring 1.2s linear infinite;
  -ms-animation: lds-dual-ring 1.2s linear infinite;
  -o-animation: lds-dual-ring 1.2s linear infinite;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

</style>
