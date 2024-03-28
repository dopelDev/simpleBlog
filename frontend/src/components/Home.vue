<template>
	<section class="container is-fluid color1">
		<MainBar />
		{{ post }}
		{{ error }}
	</section>
	<section class="section is-medium">
	</section>
</template>

<script>
	import { fetchApi } from '../custom.js';
	import MainBar from 'Components/MainBar.vue';
	export default {
		name: 'Home',
		data() {
			return { 
				post: [],
				error: null,
			}
			// data
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
@import 'Assets/scss/main.scss';
section {
	height: 100%;
	font-family: 'MartianMonoNerdFont', monospace;
}
</style>
