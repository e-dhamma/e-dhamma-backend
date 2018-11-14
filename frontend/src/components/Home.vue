<template>
  <div>
    <v-container>

      <v-layout row class='mt-5'>
        <v-flex class='text-xs-center'>
          <div id="logo-box">
            <img src="/static/img/DharmaWheel.b2a7dc4.svg" alt="logo" width='150'>
            <span id='logoText'>Paali-eesti sõnaraamat</span>
          </div>
        </v-flex>
      </v-layout>

      <v-layout class='mt-4'>
        <v-flex xs12 sm8 offset-sm2>
          <v-layout>
            <v-flex xs11>
          <v-text-field
          label="Otsi"
          v-model="searchInput"
          @keyup.enter.native="searchTerm"
          style="float:left">
          </v-text-field>
        </v-flex>
            <v-flex xs1>
          <v-btn color="primary" @click="searchTerm()"><v-icon>search</v-icon></v-btn>
        </v-flex>
      </v-layout>
        </v-flex>
      </v-layout>

      <v-layout row wrap class='mt-2'>
        <v-flex class='text-xs-center'>
          <p class='intro'>Budistliku õpetuse edasiandmiseks loodud mahukas tekstikorpus kätkeb endas keerukat terminoloogiat, mille tõlkimine
              emakeelde on läbi aegade olnud oluliseks sammuks Buddha õpetuse juurdumisel kohalikus kultuuriruumis.
              Käesolev sõnaraamat on mõeldud nii budistliku kirjanduse lugejatele kui tõlkijatele, aidates leida
              terminitele selgitusi ja tõlkevasteid ning panustades ühtse eestikeelse terminoloogia väljakujunemisse.</p>
        </v-flex>
      </v-layout>

    </v-container>

    <v-footer inset app>
      <div style="margin: auto">
        <p style="text-allign: center">See on avatud lähtekoodiga projekt. Vaata lähtekoodi <a href="https://github.com/e-dhamma/Pali-Estonian-dictionary-web-application">siit</a>.</p>
      </div>
    </v-footer>

  </div>
</template>

<script>
import { bus } from '../main.js'
export default {
  data () {
    return {
      searchInput: ''
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

<style scoped>
  .intro {
    font-size: 1.3em;
  }
  .btn {
    min-width: 40px;
  }
  #logo-box {
    display: inline-block;
  }
  img {
    vertical-align: middle;
  }
  #logoText {
    display: inline-block;
    vertical-align: middle;
    color: #cd5a07;
    font-size: 3.2em;
  }
</style>
