<template>
  <v-container>
    <v-layout>
      <v-flex xs12 sm6 offset-sm3>
        <v-card>
          <v-card-text>
            <v-container>
              <form @submit.prevent="onSingIn">
                <v-layout>
                  <v-flex>
                    <h2>Logi sisse</h2>
                  </v-flex>
                </v-layout>
                <v-layout>
                  <v-flex>
                    <v-text-field
                    name="username"
                    label="Kasutajanimi"
                    id="username"
                    v-model="username"
                    required></v-text-field>
                  <v-text-field
                    name="password"
                    label="Salasõna"
                    id="password"
                    type="password"
                    v-model="password"
                    required></v-text-field>
                    <v-btn type="submit">Logi sisse</v-btn>
                  </v-flex>
                </v-layout>
              </form>
            </v-container>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<<script>
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    onSingIn () {
      // Vuex
      console.log(this.password)
    }
  }
}
</script>



