import Vue from 'vue';
import Router from 'vue-router';
import Pessoas from '../components/Pessoas.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Pessoas',
      component: Pessoas,
    },
  ],
});
