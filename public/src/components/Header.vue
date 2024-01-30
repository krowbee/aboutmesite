<script>


</script>
<template>
  <div class="header sticky-top">
    <h2>Anton Yasinskiy</h2>
    <h3>|I am Full-Stack Developer|</h3>
    <ul>
        <RouterLink to="/" active-class="active"><li>Main</li></RouterLink>
        <RouterLink to="/aboutme" active-class="active"><li>AboutMe</li></RouterLink>
        <li>Portfolio</li>
        <RouterLink to="/skills" active-class="active"><li>Skills</li></RouterLink>
        <RouterLink to="/contacts" active-class="active"><li>Contacts</li></RouterLink>
    </ul>
  </div>
</template>

<style scoped>
h2{
    text-align: center;
    font-size: 25px;
    margin-top: 10px;
    
}

div:hover{
    cursor:default;
}


div.header{
    width: 100%;
    color:#B3B3B3;
    display: flex;
    text-align: center;
    justify-content: space-between;
    position: relative;
    background-color: #f2ffe8;
}
ul{
    float:right;
}



li:hover{
    cursor: pointer;
}



li{
    list-style: none;
    display: inline;
    margin: 5px;
    padding: 10px;
    font-size: 30px;
    font-weight: 500;
}

a{
  color: #b3b3b3;
  text-decoration: none;
}

a:hover{
    color:#E7746F;
    text-decoration: none;
}

.active{
    color:#E7746F;
    
}

.active:hover{
    color:#E7746F;
}
</style>
