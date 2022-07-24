<template>
  <HeaderCode />
  <h1>Welcome to AIFMRM ERS Dashboard Landing Page</h1>
</template>
<script>
import HeaderCode from "./HeaderCode.vue";
export default {
  name: "HomePage",
  components: {
    HeaderCode,
  },
  mounted() {
    let user = localStorage.getItem("user-info");
    if (!user) {
      this.$router.push({ name: "SignUp" });
    }
  },
};
</script>
