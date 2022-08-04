<template>
    <div class="container">
        <p>Sectors</p>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Sectors',
    data() {
        return {
            msg: ""
        };
    },
    methods : {
        getResponse(){
            const path = 'http://localhost:5000/api/sectors/available-sectors';
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