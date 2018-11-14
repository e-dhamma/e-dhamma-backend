<template>
  <v-container>
    <ul>
      <li v-for="term in terms" :key="term.id"><router-link :to="'/terminid/' + term.pali">{{ term.pali }}</router-link></li>
    </ul>
  </v-container>
</template>

<script>
  export default {
    computed: {
      terms () {
        return this.$store.getters.termList
      }
    }
  }
</script>
