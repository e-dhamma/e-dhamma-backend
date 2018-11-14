<template>
  <div>
    <v-tabs>
      <v-tabs-bar class="cyan" dark>
        <v-tabs-item ripple>
          Item
        </v-tabs-item>
        <v-tabs-item ripple>
          Item 2
        </v-tabs-item>
        <v-tabs-slider color="yellow"></v-tabs-slider>
      </v-tabs-bar>
      <v-tabs-items>
        <v-tabs-content
        >
          <v-card flat>
            <v-card-text>text</v-card-text>
                      </v-card>
        </v-tabs-content>
      </v-tabs-items>
    </v-tabs>

  <v-container>
  <v-layout>
    <v-flex>
      {{ user }}
    </v-flex>
  </v-layout>
  </v-container>
    </div>
</template>

<<script>
export default {
  data () {
    return {

    }
  },
  computed: {
    user () {
      console.log(this.$store.getters.loadedUsers, 'yes')
      return this.$store.getters.loadedUsers
    }
  }
}
</script>

