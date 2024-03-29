<template>
	<section class="container is-fluid color1">
		<MainBar />
		<h1>{{ this.posts }}</h1>
		<h1 v-if="posts && posts.length">{{ this.posts[0].title }}</h1>
		<p v-if="error">{{ error }}</p>
		<p v-if="error">{{ error }}</p>
	</section>
	<section class="section is-medium">
    <div v-for="post in posts" :key="post.id" class="card">
      <header class="card-header">
        <p class="card-header-title is-1">
          {{ post.title }}
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          {{ post.content }}
          <br>
          <time datetime="post.published">{{ post.published }}</time>
        </div>
      </div>
      <footer class="card-footer">
        <a href="#" class="card-footer-item">Share</a>
        <a href="#" class="card-footer-item">Comment</a>
      </footer>
    </div>
    <p v-if="error" class="notification is-danger">{{ error }}</p>
	</section>
</template>

<script>
	import MainBar from './MainBar.vue'; // Asegúrate de que la ruta sea correcta
	import { fetchApi } from '../custom.js'; // Asegúrate de que la ruta sea correcta
	export default {
		name: 'Home',
		data() {
			return {
				posts: [],
				error: null,
			};
		},
		async created() {
			try {
				this.posts = await fetchApi('posts');
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

