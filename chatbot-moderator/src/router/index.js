import Vue from 'vue';
import VueRouter from 'vue-router';
import Chat from '../components/Chat.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Chatbot',
    component: Chat
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
