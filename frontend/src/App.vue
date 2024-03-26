<template>
	<div id="app"></div>
	<router-view />
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import Login from './components/Login.vue';
	export default {
	name: 'App',
	components: {
		Login,
//		Mlogin,
//		Signup,
//		Msignup,
//		AuthNeeded,
//		MauthNeeded,
	},
	setup() {
		const isDesktop = ref(window.innerWidth > 1024);
		const refreshSize = () => {
			isDesktop.value = window.innerWidth > 1024;
		};
		onMounted(() => {
			window.addEventListener('resize', refreshSize);
		});
		onUnmounted(() => {
			window.removeEventListener('resize', refreshSize);
		});
		return { isDesktop };
	}
};
</script>

<style scoped lang="scss">
@import './assets/scss/main.scss';
</style>
