<template>
  <div class="container">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">Add lead</h1>
          </div>
      </div>
      <div class="column is-12">
          <form @submit.prevent="submitForm">
              <div class="field">
                  <label class="label">Company</label>
                  <input class="input" name="company" type="text" v-model="company">
              </div>
              <div class="field">
                  <label class="label">Contact person</label>
                  <input class="input" name="contact_person" type="text" v-model="contact_person">
              </div>
              <div class="field">
                  <label class="label">Email</label>
                  <input class="input" name="email" type="email" v-model="email">
              </div>
              <div class="field">
                  <label class="label">Phone</label>
                  <input class="input" name="phone" type="text" v-model="phone">
              </div>
              <div class="field">
                  <label class="label">Website</label>
                  <input class="input" name="website" type="text" v-model="website">
              </div>
              <div class="field">
                  <label class="label">Confidence</label>
                  <input class="input" name="confidence" type="number" v-model="confidence">
              </div>
              <div class="field">
                  <label class="label">Estimated value</label>
                  <input class="input" name="estimated_value" type="number" v-model="estimated_value">
              </div>
    
              <div class="field">
                  <label class="label">Status</label>
                  <div class="control">
                      <div class="select">
                        <select name="status" v-model="status">
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
                        <select name="status" v-model="priority">
                          <option value="low">Low</option>
                          <option value="medium">Medium</option>
                          <option value="high">High</option>
                          </select>
                      </div>
                  </div>
              </div>
               <div class="field">
                  <label class="label">Logo</label>
                  <div class="file">
                    <label class="file-label">
                        <input ref="file" class="file-input" type="file" name="resume" @change="handleFileUpload">
                        <span class="file-cta">
                        <span class="file-icon">
                            <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                            Choose a file…
                        </span>
                        </span>
                    </label>
                    </div>
              </div>
              <figure class="image is-128x128">
                <img :src="image" />
              </figure>

              <!-- Upload multiple files -->
              <div>
                  <input ref="files" type="file" multiple id="files" name="files" @change="handleMultipleFiles">
              </div>
              {{files}}


              <div class="field">
                  <button class="button is-success is-rounded">Submit</button>
              </div>
          </form>
      </div>
  </div>
</template>

<script>
import {toast} from 'bulma-toast'
import axios from 'axios'
export default {
    name: 'AddLead',
    data(){
        return {
            company: '',
            contact_person: '',
            email: '',
            phone: '',
            website: '',
            confidence: 0,
            estimated_value: 0,
            status: 'new',
            priority: 'medium',
            logo: '',
            image: '',
            files: ''

        }
    },
    methods: {
        handleMultipleFiles(){
            this.files = this.$refs.files.files
        },
        createImage(file) {
            let image = new Image();
            let reader = new FileReader();

            reader.onload = (e) => {
                this.image = e.target.result;
            };
            reader.readAsDataURL(file);
            },
        handleFileUpload(){
            this.logo = this.$refs.file.files[0];
            this.createImage(this.$refs.file.files[0]);
            },
        async submitForm(){
            this.$store.commit('setIsLoading', true)
            const leadData = new FormData()
            leadData.append('company', this.company)
            leadData.append('contact_person', this.contact_person)
            leadData.append('email', this.email)
            leadData.append('phone', this.phone)
            leadData.append('website', this.website)
            leadData.append('confidence', this.confidence)
            leadData.append('estimated_value', this.estimated_value)
            leadData.append('status', this.status,)
            leadData.append('priority', this.priority)
            leadData.append('logo', this.logo)

            for ( let i = 0; i < this.files.length; i++){
                let f = this.files[i]
                leadData.append('files[' + i + ']', f)
                console.log(f)
            }
            leadData.append('files_length', this.files.length)

            axios.post('/api/v1/leads/', leadData, {
                headers: {
                'content-type': 'multipart/form-data',
            }
            })
                 .then(res => {
                     console.log(res)
                     toast({
                             message: 'Added successfully',
                             type: 'is-success',
                             dismissible: true,
                             pauseOnHover: true,
                             duration: 4000,
                             position: 'bottom-right'
                         })

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