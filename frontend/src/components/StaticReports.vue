<template>
  <div>
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "StaticReports",
  data() {
    return {
      msg: "Welcome to AIFMRM ERS Dashboard Landing Page",
    };
  },
  mounted() {
    let user = localStorage.getItem("user-info");
    if (!user) {
      this.$router.push({ name: "HomePage" });
    }
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/static-reports";

      axios
        .get(path)
        .then((response) => {
          console.log(response.data);
          this.msg = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    created() {
      this.getResponse();
    },
  },
};
</script>
