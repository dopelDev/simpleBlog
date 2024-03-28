<template>
	<section class="container is-fluid color1">
		<MainBar />
		<div class="section is-medium">
			<div class="columns is-centered">
				<div class="column is-5">
					<div class="box color4">
						<form @submit.prevent="signup">
						<h1 class="title is-4 has-text-centered text-color2">Signup</h1>
							<div class="field">
								<div class="block my-4">
									<label class="label text-color2">Name</label>
									<div class="control">
										<input class="input" type="text" placeholder="Name">
									</div>
								</div>
							</div>
							<div class="field">
								<div class="block my-4">
									<label class="label text-color2">Email</label>
									<div class="control">
										<input class="input" type="email" placeholder="Email">
									</div>
								</div>
							</div>
							<div class="field">
								<div class="block my-4">
									<label class="label text-color2">Password</label>
									<div class="control">
										<input class="input" type="password" placeholder="Password">
									</div>
								</div>
							</div>
								<div class="field">
									<div class="block my-4">
										<div class="control">
											<button class="button is-primary is-fullwidth">Signup</button>
										</div>
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
	import MainBar from "./MainBar.vue"
	export default {
		name: 'Signup',
		components: {
			MainBar
		},
	}
</script>
