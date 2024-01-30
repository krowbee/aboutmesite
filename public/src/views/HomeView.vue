<script>
import Header from '../components/Header.vue'
import MainSection from '../components/MainSection.vue'
import Footer from '../components/Footer.vue'
 export default{
  data(){
    return{

    }
  },
  components:{
    Header,
    MainSection,
    Footer,
    },
 }
</script>

<template>
  <div class="section-main">
    <Header />
    <MainSection />
    <Footer />
</div>
</template>
