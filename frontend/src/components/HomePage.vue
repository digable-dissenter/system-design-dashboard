<template>
  <HeaderCode/>
  <h1>Welcome to AIFMRM ERS Dashboard Landing Page</h1>
<HomeIntro/>

</template>

<script>



import HeaderCode from './HeaderCode.vue'
import HomeIntro from './HomeIntro.vue'

export default {
    name:'HomePage',
    components: {HeaderCode,
      HomeIntro

    },

    mounted()
    {
        let user=localStorage.getItem('user-info');
        if(!user)
        {
          this.$router.push({name:'SignUp'})   
        }
    }
}
</script>

<style>


</style>