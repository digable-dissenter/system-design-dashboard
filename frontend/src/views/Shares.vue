<template>
    <div class="container">
        <p>Shares</p>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Shares',
    data() {
        return {
            msg: ""
        };
    },
    methods : {
        getResponse(){
            const path = 'http://localhost:5000/weights';
            axios.get(path)
            .then((res) => {
                console.log(res.data);
                this.msg = res.data;
            })
            .catch ((err) => {
                console.error(err);
            });
        },
    },
    created(){
        this.getResponse();
    }
}
</script>