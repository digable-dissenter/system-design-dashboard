<template>
  <div class="nav">
    <a v-on:click="home" href="#">Home</a>
    <a v-on:click="indices" href="#">Indices</a>
    <a v-on:click="sectors" href="#">Sectors</a>
    <a v-on:click="shares" href="#">Shares</a>
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
        indices(){
        this.$router.push({name:'Indices'})
        },
        sectors(){
        this.$router.push({name:'Sectors'})
        },
        shares(){
        this.$router.push({name:'Shares'})
        } 

    }
}

</script>

<style>

.nav{
  background-color:#1E71BB;
  overflow : hidden
}


</style>