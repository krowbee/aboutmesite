<script>
import axios from 'axios';
export default{
        data(){
            return{
                work_info:[]
        }
    },
    async mounted(){
    try{
      const res = await axios.get("http://127.0.0.1:8000/api/aboutwork/?format=json");
      this.work_info= res.data;
      console.warn("Получилось")
    }catch(error){
      console.error("Ошибка")
    }
  }
}
</script>

<template>
    <div class="section">
        <div>
            <h1>This is what I do</h1>
        </div>
        <div class="blocks">
            <div class="block" v-for="el,i in work_info" :key='i' >
                <img :src="'/img/'+ el.image">
                <h4>{{el.title}}</h4>
                <p>{{ el.text }}</p>
            </div>

        </div>
        <p class="something">On this site you can find out all the necessary information about me</p>
    </div>
</template>

<style scoped>



div.section{
    text-align: center;
}

div.blocks{
    display: flex;
}
div.block{
    display: inline;
    margin: 20px;
    width: 400px;
    height: 300px;
    background-color: #f2ffe8;
    border: 0.5px solid black;
    border-radius: 20px;
}
img{
    padding-top: 5px;
    width:70px
}

img:hover{
    cursor: default;
}
</style>