import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    loadedTermList: [],
    // loadedUsers: [
    //   {username: 'jüri'}
    // ],
    searchResults: []
  },
  mutations: {
    addTermList (state, termList) {
      termList.sort(function (a, b) {
        var itemA = a.pali.toUpperCase()
        var itemB = b.pali.toUpperCase()
        return (itemA < itemB) ? -1 : (itemA > itemB) ? 1 : 0
      })
      state.loadedTermList = termList
    },
    addSearchResults (state, results) {
      state.searchResults = results
    }
  },
  actions: {
    addTermList ({commit}, termList) {
      commit('addTermList', termList)
    },
    addSearchResults ({commit}, results) {
      commit('addSearchResults', results)
    }
  },
  getters: {
    // loadedUsers (state) {
    //   return state.loadedUsers
    // },
    searchForTerm (state) {
      return searchInput => {
        var results = new Set()
        state.loadedTermList.forEach((term) => {
          if (term.pali.toLowerCase().includes(searchInput.toLowerCase())) { results.add(term) }
          term.meaning_set.forEach((meaning) => {
            if (meaning.est.toLowerCase().includes(searchInput.toLowerCase())) { results.add(term) }
            if (meaning.eng.toLowerCase().includes(searchInput.toLowerCase())) { results.add(term) }
          })
        })
        return Array.from(results)
      }
    },
    searchResults (state) {
      return state.searchResults
    },
    termList (state) {
      return state.loadedTermList
    }
  }
})
