

<template>

  <!-- ref: https://www.anthropic.com/ -->

  <!-- Hero start -->
  <div class="hero"
    style="background-image: url(https://daisyui.com/images/stock/photo-1507358522600-9f71e620c44e.jpg); min-height: 60vh;">
    <div class="hero-overlay bg-opacity-60"></div>
    <div class="text-neutral-content">
      <a-row>
        <!-- 左则介绍 -->
        <a-col :span="16">

          <div class="text-6xl">Explore mesenchymal stem cell in</div>
          <div class="text-6xl mt-4">MSCs<span>Atlas</span></div>


          <div class="text-xl mt-4">
            A database of mesenchymal stem cells sequencing data
          </div>

          <div class="text-xl">
            contain information from
          </div>

        </a-col>
      </a-row>

    </div>
  </div>
  <!-- Hero end -->

  <!-- Function start -->
  <div class="bg-base-200">

    <div class="min-w-screen-lg max-w-screen-xl mx-auto">
      <h2 class="text-center text-3xl py-8">Feature</h2>
      <a-row :gutter="20">
        <a-col v-for="i in 4" :key="i" :span="6">
          <div class="card bg-base-100 shadow-xl">
            <div class="h-40 pt-4">
              <figure><img :src="functions[i-1].fig" alt="Shoes" /></figure>
            </div>
            
            <!-- <figure><img src="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg" alt="Shoes" /></figure> -->
            <div class="card-body">
              <h2 class="card-title">
                {{ functions[i-1].title }}
                <div class="badge badge-secondary">NEW</div>
              </h2>
              <p class="h-32">{{ functions[i-1].description  }}</p>
              <div class="card-actions justify-end">
                <div class="badge badge-outline">See more</div>
              </div>
            </div>
          </div>
        </a-col>
      </a-row>
    </div>


  </div>
</template>

<script>
export default {
  data() {
    return {
      functions: [
        { title: "Browser", description: "Browser the data", fig: "/batchsearch.svg"},
        { title: "Gene expression", description: "check the gene expression", fig: "/cell.svg"},
        { title: "Patrhway activity", description: "check the Patrhway activity", fig: "/download.svg" },
        { title: "Function assess", description: "Access your sample function", fig: "/increase.svg" },
      ]
    }
  }
}
</script>