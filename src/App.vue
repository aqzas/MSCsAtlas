<style scoped>

a {
  color: inherit;
  text-decoration: none;
}

a:hover {
  color: inherit;
  text-decoration: none;
}

li {
  font-size: 16px;
  font-weight: bold;
}

</style>

<template>
  <div style="background-color: #F0F0EB;" class="font-serif">

    <!-- header menu -->

    <div class="navbar" style="background-color: #F0F0EB; z-index: 50;" >
      <div class="flex-1">
        <router-link to="/" class="btn btn-ghost text-3xl">MSCAtlas</router-link>
      </div>
      
      <ul class="menu menu-horizontal mb-0">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/assess">Assess</router-link></li>
        <li>
          <details v-bind:open="openFlag">
            <summary>Browse data</summary>
            <ul style="z-index: 100;">
              <li><router-link to="/dashboard" @click="openFlag = false">Datasets</router-link></li>
              <li><router-link to="/expression" @click="openFlag = false">Gene Expression</router-link></li>
              <li><router-link to="/enrichment" @click="openFlag = false">Genesets ssGSEA</router-link></li>
            </ul>
          </details>
        </li>
        <li><router-link to="/document">Document</router-link></li>
       
      
       
      </ul>
      
    </div>

    <!-- content view -->

    <div class="pt-8">
      <router-view />
    </div>

    <!-- footer -->
    <footer class="footer footer-center p-10 text-base-content rounded bg-slate-300" >
      <aside>
        <p>Copyright © 2023 - Union Cell Lab, Union Hospital, HUST, China</p>
        <p>Any comments and suggestions, please contact us.</p>
      </aside>
    </footer>

  </div>
</template>


<script>

export default {
  data() {
    return {
     
      openFlag: false,
    };
  },
};
</script>

<style></style>


