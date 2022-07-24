<template>
  <div class="nav">
    <a href="#">Home</a>
    <a href="#">Static Reports</a>
    <a v-on:click="logout" href="#">Logout</a>
  </div>
</template>

<script>
export default {
  name: "HeaderCode",
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push({ name: "LoginPage" });
    },
  },
};
</script>
<style>
.nav {
  background-color: #1e71bb;
  overflow: hidden;
}
</style>
