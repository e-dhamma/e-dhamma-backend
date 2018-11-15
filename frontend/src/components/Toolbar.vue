<template>
  <v-toolbar
  :clipped-left="$vuetify.breakpoint.lgAndUp"
  app
  fixed
  >
    <!-- For navigation drawer on small screens -->
    <!-- <v-btn icon @click.stop='rightDrawer = !rightDrawer' class='hidden-sm-and-up'>
      <v-icon>menu</v-icon>
    </v-btn> -->
    <v-toolbar-title class='hidden-xs-only'>
      <v-avatar>
        <img src="../../static/DharmaWheel.svg" alt="dhamma-wheel">
      </v-avatar>
      <router-link to='/' tag='span' style='cursor: pointer'>Paali-eesti sõnaraamat</router-link>
    </v-toolbar-title>

      <!-- Spacer -->
      <div style="width: 85px;"></div>
      <!-- Search -->
      <template v-if="!isHomepage">
        <v-text-field label="Otsi" v-model="searchInput" @keyup.enter.native="searchTerm"></v-text-field>
        <!-- <v-autocomplete
          :items="[1, 2]">
        </v-autocomplete> -->
        <v-btn icon @click="searchTerm" color="primary"><v-icon>search</v-icon></v-btn>
      </template>
      <v-spacer></v-spacer>
      <!-- <v-btn
      flat
      v-for='item in menueItems' :key='item.title'>
        <v-icon left>{{ item.icon }}</v-icon>
        {{ item.title }}
      </v-btn> -->
  </v-toolbar>
</template>

<script>
import { bus } from '../main.js'
export default {
  data () {
    return {
      searchInput: ''
      // // For navigation drawer for small screen
      // rightDrawer: false,
      // // Toolbar buttons
      // menueItems: [
      //   { icon: 'toc', title: 'Rohkem', link: '' },
      //   { icon: 'notifications', title: 'Teavitused', link: '' },
      //   { icon: 'account_circle', title: 'Logi sisse', link: '' }
      // ]
    }
  },
  computed: {
    isHomepage () {
      var path = this.$route.path
      if (path === '/') { return true }
      return false
    }
  },
  methods: {
    searchTerm () {
      if (this.searchInput === '') { return null }
      bus.$emit('searchTerm', this.searchInput)
      this.searchInput = ''
    }
  }
}
</script>
