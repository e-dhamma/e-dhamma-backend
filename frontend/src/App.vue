<template>
  <v-app>
    <!-- Term-list -->
    <term-list-navigation-drawer></term-list-navigation-drawer>
    <!-- Toolbar -->
    <toolbar></toolbar>

    <!-- For small screen -->
    <!-- <v-navigation-drawer
      temporary
      v-model='rightDrawer'
      fixed>
      <v-list>
        <v-list-tile v-for='item in menueItems' :key='item.title'>
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer> -->

    <!-- Snackbar for notifications -->
    <v-snackbar
      :timeout="3000"
      :top="true"
      v-model="snackbar"
    >
      {{ notification }}
      <v-btn flat color="pink" @click.native="snackbar = false">Sulge</v-btn>
    </v-snackbar>

    <!-- Main content -->
    <v-content>
      <router-view :key="$route.fullPath"></router-view>
    </v-content>
    <search></search> <!-- This component does not have a template, only methods -->

  </v-app>
</template>

<script>
  import NavigationDrawer from './components/TermListNavigationDrawer'
  import Toolbar from './components/Toolbar'
  import Search from './components/Search'
  import { bus } from './main.js'
  export default {
    data () {
      return {
        // For snackbar
        snackbar: false,
        notification: ''
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
    created () {
      bus.$on('showNotification', (notification) => { this.showNotification(notification) })
    },
    components: {
      'term-list-navigation-drawer': NavigationDrawer,
      'toolbar': Toolbar,
      'search': Search
    },
    methods: {
      showNotification (notification) {
        this.notification = notification
        this.snackbar = true
      }
    }
  }
</script>
