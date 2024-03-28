<template>
	<section class="container is-fluid color1">
		<MainBar />
		<h1>{{ this.post }}</h1>
		    <h1 v-if="post && post.length">{{ post[0].title }}</h1>
    <p v-if="error">{{ error }}</p>
		<p v-if="error">{{ error }}</p>
	</section>
	<section class="section is-medium">
	</section>
</template>

<script>
	import MainBar from './MainBar.vue'; // Asegúrate de que la ruta sea correcta
	import { fetchApi } from '../custom.js'; // Asegúrate de que la ruta sea correcta
	export default {
		name: 'Home',
		data() {
			return {
				post: [],
				error: null,
			};
		},
		async created() {
			try {
				this.post = await fetchApi('posts');
			} catch (error) {
				this.error = error.toString();
			}
		},
		components: {
			MainBar,
		}
	};
</script>

<style lang="scss">
@import '@/assets/scss/main.scss'; // Asegúrate de que la ruta sea correcta

	section {
		height: 100%;
		font-family: 'MartianMonoNerdFont', monospace;
	}
</style>

