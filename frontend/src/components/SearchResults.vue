<template>
  <v-container>
    <v-layout>
      <v-flex>
        <h2>Sinu otsingusõnaga andis mitu vastet</h2>
      </v-flex>
    </v-layout>
    <v-flex>
      <ul>
        <li v-for="result in results" :key="result.id">
          <router-link :to="'/terminid/' + result.slug">pl: <i>{{ result.pali }}</i>; est: {{ result.est }};</router-link>
        </li>
      </ul>
    </v-flex>
    <v-layout>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  computed: {
    results () {
      return this.$store.getters.searchResults
    }
  }
}
</script>
