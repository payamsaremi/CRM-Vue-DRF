<template>
  <div class="container">
      <section class="hero is-small is-light">  
  <div class="hero-body is-flex is-justify-content-space-between">
    <div class="is-flex is-justify-content-start">
        <!-- <figure class="image is-128x128">
           <img class="is-rounded" :src="lead.logo" alt="">
        </figure> -->
        <p class="title">
            {{lead.company}}
        </p>
    </div>
    <p class="subtitle">
        <router-link :to="{ name: 'EditLead', params: { id: lead.id } }" class="button is-black">Edit</router-link>
    </p>
  </div>
</section>
      <div class="columns is-multiline is-variable is-1-mobile is-0-tablet is-3-desktop is-8-widescreen is-2-fullhd">
          <div class="column is-12">
              
          </div>
          <div class="column is-6">
              <div class="box">
                  <h2 class="subtitle">contact information</h2>
                  <p>company: <strong>{{ lead.company }}</strong></p>
                  <p>Contact person: <strong>{{ lead.contact_person }}</strong></p>
                  <p>Email: <strong>{{ lead.email }}</strong></p>
                  <p>Phone: <strong>{{ lead.phone }}</strong></p>
                  <p>Website: <strong>{{ lead.website }}</strong></p>
              </div>
          </div>
          <div class="column is-6">
              <div class="box">
                  <h2 class="subtitle">more Information</h2>
                  <p>Confidence: <strong>{{ lead.confidence }}</strong></p>
                  <p>Estimated value: <strong>{{ lead.estimated_value }}</strong></p>
                  <p>Status: <strong>{{ lead.status }}</strong></p>
                  <p>Priority: <strong>{{ lead.priority }}</strong></p>
                  <p>created at: <strong>{{ lead.created_at }}</strong></p>
                  <p>modified at: <strong>{{ lead.modified_at }}</strong></p>
                  
              </div>
          </div>
      </div>
            <div class="columns flex-wrap is-multiline ">
                <div v-for="image in lead.images" :key="image.id" >
                    <div class="">
                        <div class="column">
                        <div class="box" style="width: 300px">
                            <a @mouseenter.prevent="setLightBox" :href="image.image" class="glightbox">
                                <figure class="image ">
                                <img :src="image.image" >
                                </figure>
                            </a>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
  </div>
</template>

<script>
import GLightbox from 'glightbox'
import axios from 'axios'

export default {
    name: 'Lead',
    data(){
        return {
            lead: {},
            lightbox: ''
        }
    },
    mounted(){
        this.getLead()
    },
    methods: {
        async getLead(){
            this.$store.commit('setIsLoading', true)
            const leadId = this.$route.params.id

            await axios.get(`/api/v1/leads/${leadId}/`)
                 .then( res => {
                     this.lead = res.data
                    //  console.log(res.data)
                 })
                 .catch (err => {
                     console.log(err)
                 })

            this.$store.commit('setIsLoading', false)
        },
        setLightBox(){
            this.lightbox = GLightbox({
                touchNavigation: true,
                loop: true,
            })
        },
        toggleLightBox(){
            
            this.lightbox.open()
        }
    }

}
</script>

<style>

</style>