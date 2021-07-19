<template>
  <div class="container">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">Leads</h1>
              <router-link to="/dashboard/leads/add" class="button is-link is-rounded">Add Lead</router-link>
          </div>
          <div class="table-container column is-12">
              <table class="table is-fullwidth">
                  <thead>
                      <tr>
                          <th> </th>
                          <th>ID</th>
                          <th>Company</th>
                          <th>Contact person</th>
                          <th>Status</th>
                          <th>Website</th>
                          <th>Phone</th>
                          <th>Status</th>
                          <th>Priority</th>
                          <th> </th>
                      </tr>
                  </thead>
                  <tbody>
                      <tr
                      v-for="lead in leads"
                      :key="lead.id"
                      >
                       
                        <td>
                            <router-link :to="{ name: 'Lead', params: { id: lead.id } }">
                                <span>
                                    <figure class="image is-48x48"><img  :src="lead.logo" alt=""></figure>
                                </span>
                            </router-link>
                        </td>
                        
                        <td>{{ lead.id }}</td>
                        <td>{{ lead.company }}</td>
                        <td>{{ lead.contact_person }}</td>
                        <td>{{ lead.status }}</td>
                        <td>{{ lead.website }}</td>
                        <td>{{ lead.phone }}</td>
                        <td ><span class="tag is-info is-light">{{ lead.status }}</span></td>
                        <td ><span class="tag is-light">{{ lead.priority }}</span></td>
                        <td><router-link :to="{ name: 'Lead', params: { id: lead.id } }"><span class="button is-small is-link is-outlined">View</span></router-link></td>
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
    name: 'Leads',
    data(){
        return {
            leads: []
        }
    },
    mounted() {
        this.getLeads()
    },
    methods: {
        async getLeads(){
            this.$store.commit('setIsLoading', true)
            await axios.get('/api/v1/leads/')
                 .then(res => {
                    this.leads = res.data
                 })
                 .catch(err => {
                     console.log(err)
                 })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style>

</style>