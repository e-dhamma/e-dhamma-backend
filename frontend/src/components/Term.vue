<template>
  <div>
    <!-- Loading -->
    <v-container v-if="loading">
      <v-layout>
          <v-flex class="text-xs-center">
            <v-progress-circular
              :size="70"
              color="primary"
              indeterminate
              width="6"
            ></v-progress-circular>
          </v-flex>
      </v-layout>
    </v-container>

    <v-container v-else>
      <!-- term metadata -->
      <v-layout>
          <v-flex>
              <h4 v-if="loading">Loading...</h4>
              <h1><i>{{ term.pali }}</i></h1>
              <p><template v-if="term.wordClass || term.gender">({{ term.wordClass }}, {{ term.gender }}) </template><!--<i>hääldus</i> <v-icon>play_arrow</v-icon>--></p>
          </v-flex>
      </v-layout>
      <!-- term meanings -->
      <v-layout v-for='(meaning, i) in term.meaning_set' :key='i' class='mt-3'>
          <v-flex>
              <h3>{{ i + 1}}. {{ meaning.est }}<template v-if="meaning.root"> [{{ meaning.rootLang }} <i>{{ meaning.root }}</i><template v-if="meaning.rootDescription"> ({{ meaning.rootDescription}})</template>]</template></h3>
              <template v-if="meaning.eng"><p>eng {{ meaning.eng }}</p></template>
              <p>{{ meaning.expl }}</p>
              <template v-if="meaning.further || meaning.example_set.length != 0">
                  <v-expansion-panel>
                    <v-expansion-panel-content>
                        <div slot="header" class="further-explanation">Täpsemalt</div>
                        <v-card>
                            <v-card-text style="background-color: #f4f1ef">
                                <p>{{ meaning.further }}</p>
                                <template v-if="meaning.example_set.length != 0"><h4>Tõlkenäited:</h4></template>
                                <div>
                                    <p v-for='example in meaning.example_set' :key='example.original'>
                                        <i>{{ example.original }}</i><br>
                                        {{ example.translation }}
                                    </p>
                                </div>
                            </v-card-text>
                        </v-card>
                    </v-expansion-panel-content>
                </v-expansion-panel>
              </template>
          </v-flex>
      </v-layout>
      <!-- Term definition in the Pali Text Society dictionary -->
      <template v-if="term.def_in_PLS_dict">
        <v-layout>
          <v-flex>
            <v-expansion-panel>
                <v-expansion-panel-content>
                    <div slot="header" id="pls-header">Selgitus <i>Pali Text Society</i> sõnaraamatus</div>
                    <v-card>
                        <v-card-text style="background-color: #f4f1ef">
                            <p>{{ term.def_in_PLS_dict }}</p>
                        </v-card-text>
                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
          </v-flex>
        </v-layout>
      </template>
      <!-- Comments-->
      <h2 class='comment-section-header mt-4'>{{numberOfApprovedComments}} kommentaar<template v-if="numberOfApprovedComments != 1">i</template></h2>
      <hr>
      <div v-for='(comment, i) in term.comment_set' :key='"c" + i' v-if="comment.approved == true || comment.preview" class='mt-2'>
        <p><b>{{ comment.author }}:</b> {{ comment.content}}<br>{{ comment.timestamp | date }}</p>
      </div>
      <!-- Add comment form-->
      <hr>
      <comment-form :termID="term.id" @commentAdded="showComment($event)"></comment-form>
    </v-container>
  </div>
</template>

<script>
import { bus } from '../main.js'
import { API } from '../api'
import CommentForm from './CommentForm'
export default {
  created () {
    this.loading = true
    API.getTerm(this.slug).then(response => {
      this.term = response.data
      this.loading = false
    })
  },
  props: ['slug'],
  mounted () {
    bus.$emit('termChange', this.slug)
  },
  data () {
    return {
      term: { comment_set: [] },
      loading: false
    }
  },
  components: {
    'comment-form': CommentForm
  },
  computed: {
    numberOfApprovedComments () {
      var count = this.term.comment_set.filter(comment => comment.approved)
      return count.length
    }
  },
  methods: {
    showComment (comment) {
      this.term.comment_set.push(comment)
    }
  }
}
</script>

<style scoped>
  .comment-section-header {
    font-weight: normal
  }
  /* Styles term's further information expansion-panel */
  .expansion-panel {
    box-shadow: none;
    -webkit-box-shadow: none;
  }
  .theme--light .expansion-panel .expansion-panel__container, .application .theme--light.expansion-panel .expansion-panel__container {
    background-color: inherit;
  }
  .further-explanation {
    color: #cd5a07; /* primary */
  }
  #pls-header {
    color: #cd5a07; /* primary */

  }
</style>

<style>
  /* Styles term's further information expansion-panel */
  .expansion-panel__header {
    padding-left: inherit;
  }
</style>

