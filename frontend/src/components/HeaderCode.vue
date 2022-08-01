<template>
<div class="nav">
<a v-on:click="home" href="#">Home</a>
<a href="#">Static Reports</a>
<a v-on:click="faq" href="#">FAQ's</a>
<a v-on:click="logout" href="#">Logout</a>

</div>
</template>

<script>


export default {

    name: 'HeaderCode',

    methods:{
        logout(){
        localStorage.clear();
        this.$router.push({name:'LoginPage'})
        },
        faq(){
        this.$router.push({name:'FaqPage'})
        },
        home(){
        this.$router.push({name:'HomePage'})
        },
        


        
    }
}

</script>

<style>

.nav{
  background-color:#1E71BB;
  overflow : hidden
}


</style>