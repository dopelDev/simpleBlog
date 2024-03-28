import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Signup from './components/Signup.vue';

const	routes = [
		{ 
			path: '/',
			component: Home, 
			name: 'home'
		},
		{ 
			path: '/login',
			component: Login,
			name: 'login'
		},
		{
			path: '/Signup',
			component: Signup,
			name: 'signup'
		}
];

const router = createRouter({
	history: createWebHistory('/'),
	routes
});

export default router;
