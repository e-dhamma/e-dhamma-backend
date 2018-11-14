<template>
  <v-container>
    <v-layout>
      <v-flex xs12 sm6 offset-sm3>
        <v-card>
          <v-card-text>
            <v-container>
              <form @submit.prevent="onSingUp">
                <v-layout>
                  <v-flex>
                    <h2>Registreeru kasutajaks</h2>
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
                    name="email"
                    label="Email"
                    id="email"
                    type="email"
                    v-model="email"
                    required></v-text-field>
                  <v-text-field
                    name="password"
                    label="Salasõna"
                    id="password"
                    type="password"
                    v-model="password"
                    required></v-text-field>
                    <v-text-field
                    name="confirmPassword"
                    label="Salasõna uuesti"
                    id="confirmPassword"
                    type="password"
                    v-model="confirmPassword"
                    :rules="[comparePasswords]"
                    ></v-text-field>
                    <v-btn type="submit">Registreeru</v-btn>
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

<script>
export default {
  data () {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: ''
    }
  },
  computed: {
    comparePasswords () {
      if (this.password !== this.confirmPassword) { return 'Salasõnad ei kattu' } else { return '' }
    }
  },
  methods: {
    onSingUp () {
      // Vuex
      console.log(this.password, this.confirmPassword)
    }
  }
}
</script>



