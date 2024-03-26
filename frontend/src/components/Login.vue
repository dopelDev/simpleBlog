<template>
	<section class="section">
		<div class="container">
			<div class="columns is-centered">
				<div class="column is-5-tablet is-4-desktop is-3-widescreen">
					<form @submit.prevent="login" class="box">
						<div class="field">
							<label for="username" class="label">Nombre de Usuario</label>
							<div class="control has-icons-left">
								<input type="text" id="username" class="input" required v-model="username" placeholder="e.g. johndoe">
								<span class="icon is-small is-left">
									<i class="fa fa-user"></i>
								</span>
							</div>
						</div>

						<div class="field">
							<label for="password" class="label">Contraseña</label>
							<div class="control has-icons-left">
								<input type="password" id="password" class="input" required v-model="password" placeholder="*******">
								<span class="icon is-small is-left">
									<i class="fa fa-lock"></i>
								</span>
							</div>
						</div>

						<div class="field">
							<button type="submit" class="button is-success">
								Iniciar Sesión
							</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
	export default {
		name: 'Login',
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
