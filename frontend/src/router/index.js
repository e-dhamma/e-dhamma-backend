import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Term from '@/components/Term'
import TermList from '@/components/TermList'
import LetterToAdmin from '@/components/LetterToAdmin'
// import SignIn from '@/components/SignIn'
// import UserPage from '@/components/UserPage'
import SearchResults from '@/components/SearchResults'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/terminid/:slug',
      props: true,
      name: 'Term',
      component: Term
    },
    {
      path: '/otsing/',
      props: true,
      name: 'SearchResults',
      component: SearchResults
    },
    {
      path: '/kiri-haldajale',
      name: 'LetterToAdmin',
      component: LetterToAdmin
    },
    {
      path: '/loetelu',
      name: 'TermList',
      component: TermList
    }
    // {
    //   path: '/registreeru',
    //   name: 'SignUp',
    //   component: SignUp
    // },
    // {
    //   path: '/logi-sisse',
    //   name: 'SignIn',
    //   component: SignIn
    // },
    // {
    //   path: '/kasutajaleht',
    //   name: 'UserPage',
    //   component: UserPage
    // },
    // {
    //   path: '/kasutajale',
    //   name: 'InfoForUser',
    //   component: InfoForUser
    // },
    // {
    //   path: '/haldajale',
    //   name: 'ForAdmin',
    //   component: ForAdmin
    // }
  ]
  // mode: 'history'
})
