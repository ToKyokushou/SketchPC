import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import sketchPC from '@/pages/sketchPC'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    // {
    //   path: '/',
    //   redirect: '/sketchPC',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    // {
    //   path: '/sketchPC',
    //   name: 'sketchPC',
    //   component: sketchPC
    // },
    {
      path: '/',
      name: 'sketchPC',
      component: sketchPC
    }
  ]
})
