<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import SkillsSection from '../components/SkillsSection.vue'
 export default{
  data(){
    return{

    }
  },
  components:{
    Header,
    Footer,
    SkillsSection,
    },
 }
</script>

<template>
  <div class="section-main">
    <Header />
    <SkillsSection />
    <Footer />
</div>
</template>