<template>
  <div>
    <v-layout mt-3><v-flex><h2 class="form-header">Lisa uus kommentar</h2></v-flex></v-layout>
    <v-layout row>
      <v-flex xs12 sm4>
        <v-text-field
          name="author"
          label="Nimi"
          id='author'
          v-model='author'
          required
        ></v-text-field>
      </v-flex>
      <v-flex xs12 sm4>
        <v-text-field
          name="email"
          label="E-mail"
          id='email'
          hint="Ei kuvata avalikult"
          v-model='email'
          required
        ></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs12 sm6>
        <v-text-field
          name="message"
          label="Sõnum"
          id='message'
          v-model='message'
          required
          multi-line
        ></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex>
        <v-btn :disabled='!isFormValid' @click.native='addComment' color="primary">Lisa kommentaar</v-btn>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import { API } from '../api'
export default {
  props: ['termID'],
  data () {
    return {
      author: '',
      email: '',
      message: ''
    }
  },
  computed: {
    isFormValid () {
      return this.author !== '' && this.email !== '' && this.message !== ''
    },
    isEmailValid () {
      // eslint-disable-next-line
      var re = /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
      return re.test(this.email)
    }
  },
  methods: {
    addComment () {
      if (!this.isEmailValid) {
        alert('Sisesta kehtiv email.')
        return
      }
      const comment = {
        term: this.termID,
        author: this.author,
        email: this.email,
        content: this.message,
        timestamp: new Date()
      }
      API.addComment(comment).then(() => {
        comment.preview = true
        this.$emit('commentAdded', comment)
        // this.term.comment_set.push(comment)
      }).catch(() => {
        alert('Tekkis viga. Sinu kommentaar ei salvestunud.')
      })
      this.author = ''
      this.email = ''
      this.message = ''
    }
  }
}
</script>

<style scoped>
  .form-header {
    font-weight: normal
  }

</style>
