<template>
  <div class="container">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">Edit {{ lead.company }}</h1>
          </div>
      </div>
      <div class="column is-12">
          <form @submit.prevent="submitForm">
              <div class="field">
                  <label class="label">Company</label>
                  <input class="input" name="company" type="text" v-model="lead.company">
              </div>
              <div class="field">
                  <label class="label">Contact person</label>
                  <input class="input" name="contact_person" type="text" v-model="lead.contact_person">
              </div>
              <div class="field">
                  <label class="label">Email</label>
                  <input class="input" name="email" type="email" v-model="lead.email">
              </div>
              <div class="field">
                  <label class="label">Phone</label>
                  <input class="input" name="phone" type="text" v-model="lead.phone">
              </div>
              <div class="field">
                  <label class="label">Website</label>
                  <input class="input" name="website" type="text" v-model="lead.website">
              </div>
              <div class="field">
                  <label class="label">Confidence</label>
                  <input class="input" name="confidence" type="number" v-model="lead.confidence">
              </div>
              <div class="field">
                  <label class="label">Estimated value</label>
                  <input class="input" name="estimated_value" type="number" v-model="lead.estimated_value">
              </div>
              <div class="field">
                  <label class="label">Status</label>
                  <div class="control">
                      <div class="select">
                        <select name="status" v-model="lead.status">
                          <option value="new">New</option>
                          <option value="contacted">Contacted</option>
                          <option value="inprogress">In progress</option>
                          <option value="lost">Lost</option>
                          <option value="won">Won</option>
                        </select>
                      </div>
                  </div>
              </div>
              <div class="field">
                  <label class="label">Priority</label>
                  <div class="control">
                      <div class="select">
                        <select name="status" v-model="lead.priority">
                          <option value="low">Low</option>
                          <option value="medium">Medium</option>
                          <option value="high">High</option>
                          </select>
                      </div>
                  </div>
              </div>
              <div class="field">
                  <label class="label">Priority</label>
                  <button class="button is-success is-rounded">Update</button>
              </div>
          </form>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
    name: 'EditLead',
    data(){
        return {
            lead:{}
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
                 })
                 .catch (err => {
                     console.log(err)
                 })

            this.$store.commit('setIsLoading', false)
        },
        async submitForm(){
            this.$store.commit('setIsLoading', true)
            const leadId = this.$route.params.id

            axios.patch(`/api/v1/leads/${leadId}/`, this.lead)
                 .then(res => {
                    //  console.log(res)
                     toast({
                             message: 'Updated successfully',
                             type: 'is-success',
                             dismissible: true,
                             pauseOnHover: true,
                             duration: 4000,
                             position: 'bottom-right'
                         })

                     this.$router.push(`/dashboard/leads/${leadId}`)
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