<template>

  <div>
   
     <!-- header menu -->
     <div>
      <a-menu
        mode="horizontal"
        v-model:selectedKeys="selectedKeys"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1"><router-link to="/">Home</router-link></a-menu-item>
        <a-menu-item key="2"><router-link to="/dashboard">Dashboard</router-link></a-menu-item>
      </a-menu>
     </div>
      
    <!-- content view -->

    <div style="padding-top: 20px">
      <router-view />
    </div>    
   


    <!-- footer -->
    <div style="text-align: center">
      Ant Design ©2018 Created by Ant UED
    </div>

  </div>
 
  
</template>


<script>


   export default {
    data() {
        return {
            selectedKeys: ""
        };
    },

    // watch: {
    //   selectedKeys(newValue) {
    //     this.$route.push
    //   }
    // }
};
</script>

<style>

</style>


