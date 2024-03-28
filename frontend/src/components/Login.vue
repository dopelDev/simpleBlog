<template>
	<section class="container is-fluid color1">
		<MainBar />
		<div class="section is-medium">
			<div class="columns is-centered">
				<div class="column is-5">
					<div class="box color4">
						<form @submit.prevent="login">
							<h1 class="title is-4 has-text-centered text-color2">Login</h1>
							<div class="field">
								<div class="block my-4">
									<label for="username" class="label text-color2">Username</label>
									<input type="text" id="username" class="input" required v-model="username" placeholder="Username">
								</div>
							</div>
							<div class="field">
								<div class="block my-4">
									<label for="password" class="label text-color2">Password</label>
									<input type="password" id="password" class="input" required v-model="password" placeholder="*******">
								</div>
							</div>
							<div class="field">
								<div class="block my-4">
									<button type="submit" class="button is-success">
										Login
									</button>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
	import MainBar from 'Components/MainBar.vue';
	export default {
		name: 'Login',
		components: {
			MainBar
		},
		data() {
			return {
				username: '',
				password: ''
			}
		},
		methods: {
			login() {
				this.$store.dispatch('login', {
					username: this.username,
					password: this.password
				})
			}
		}
	}
</script>

<style lang="scss">
</style>
