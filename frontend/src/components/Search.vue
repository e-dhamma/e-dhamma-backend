<template>
<p>h</p>
</template>

<script>
import { bus } from '../main.js'
export default {
  created () {
    bus.$on('searchTerm', (searchInput) => {
      this.searchTerm(searchInput)
    })
  },
  methods: {
    searchTerm (searchInput) {
      const results = this.$store.getters.searchForTerm(searchInput)
      if (results.length === 0) {
        bus.$emit('showNotification', 'Otsing ei andnud tulemusi.')
        return null
      } else if (results.length === 1) {
        this.$router.push({ name: 'Term', params: { slug: results[0].slug } })
      } else if (results.length > 1) {
        this.$store.dispatch('addSearchResults', results)
        this.$router.push({ name: 'SearchResults' })
      }
    }
  }
}
</script>
