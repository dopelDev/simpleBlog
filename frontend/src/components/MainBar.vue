<template>
	<section class="section color5 mx-6">
		<div class="columns">
			<div class="column is-10">
				<div class="hero">
					<router-link to='/' class="title text-color3">Blog</router-link>
				</div>
			</div>
			<div class="column is-2">
				<div class="columns">
					<div class="column">
						<router-link to="/login" class="button is-primary is-fullwidth">Login</router-link>
					</div>
					<div class="column">
						<router-link to="/signup" class="button is-primary is-fullwidth">Signup</router-link>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
export default {
	name: 'MainBar',
}
</script>

<style>
</style>
