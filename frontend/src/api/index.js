import Axios from 'axios'
import Cookies from 'js-cookie'

export function createConfigWithCsrfToken () {
  var csrftoken = Cookies.get('csrftoken')
  var config = csrftoken ? { headers: { 'X-CSRFToken': csrftoken } } : null
  return config
}

export const API = {
  axios: Axios.create({baseURL: '/api/', timeout: 5000}),
  // GET
  getTermList () { return this.axios.get('term-list/') },
  getTerm (slug) { return this.axios.get('single-term/' + slug + '/') },
  // POST
  addComment (comment) { return this.axios.post('term-comment/', comment, createConfigWithCsrfToken()) }
}
