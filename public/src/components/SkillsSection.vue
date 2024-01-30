<script>
import axios from 'axios';
export default{
    data(){
        return{
            skills:[]
        }
    },
    async mounted(){
        try{
           const res = await axios.get('http://127.0.0.1:8000/api/myskill/?format=json') 
           console.warn("Получилось достать скиллы")
           this.skills = res.data;
        }catch(error){
            console.error("Беда")
        }
    }
}
</script>

<template>
    <div class="section">
    <h1>What do I use in my projects</h1>
    <p></p>
    <div class="blocks">
        <div class="block" v-for="skill,i in skills" :key="i">
            <img :src="'/img/'+skill.image">
            <h4>{{ skill.title }}</h4>
            <p>{{ skill.text }}</p>
        </div>
    </div>
    <p>If you would like to contact me, choose the most convenient contact method for you on the Contacts page</p>
    </div>
</template>

<style scoped>

img:hover{
    cursor: default;
}

h4{
    font-size: 28px;
    font-weight: 600;
}

p{
    font-size: 23px;
    font-weight: 500;
}

div.section{
    text-align: center;
}

div.blocks{
    display: flex;
    text-align: center;
}
div.block{
    display: inline;
    margin: 20px;
    width: 600px;
    height: 300px;
    background-color: #f2ffe8;
    border: 0.5px solid black;
    border-radius: 20px;
}
img{
    padding-top: 5px;
    width:70px
}

</style>