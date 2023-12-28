

<template>
  <!-- ref: https://www.anthropic.com/ -->

  <!-- Bento start -->
  <div style="background-color: #F0F0EB; min-height: 90vh;">
    <div class="max-w-screen-xl mx-auto min-w-max">

      <div class="grid grid-cols-12 gap-6 py-4 mx-auto">
        <div class="bento col-span-7 h-64 rounded-3xl bg-white p-6 shadow-xl transition hover:shadow-2xl">
          <div class="text-4xl">Analysis Mesenchymal Stem Cell data</div>

          <a-config-provider :theme="{
            token: {
              colorPrimary: '#CC775C'
            }
          }">


            <a-steps class="mt-8" label-placement="vertical" :current="currentStep" :items="[
              {
                title: 'Upload file',
                description: 'Upload gene epxresion in TPM',
              },
              {
                title: 'Select analysis',
                description: 'Perform ssGESA on selected gensets',
              },
              {
                title: 'Get results',
                description: 'Visualize results compare with other samples',
              },
            ]"></a-steps>

          </a-config-provider>

        </div>

        <div class="bento col-span-5 h-64 rounded-3xl bg-white p-6 shadow-xl transition hover:shadow-2xl">
          <span class="text-4xl">Function Assess</span>
          <div id="functionbar" class="h-64 w-full" ></div>
        </div>

        <div
          class="bento col-span-4 h-48 rounded-3xl bg-white p-6 shadow-xl text-center transition hover:bg-base-200 seesee hover:shadow-2xl cursor-pointer"
          v-on:click="myaddRoute('assess')"
        >
          <h1 class="text-4xl transition" style="margin-top: 50px;">Qucik start</h1>
        </div>
        <div class="bento col-span-4 h-48 rounded-3xl p-6 shadow-xl text-center transition "
          style="background-color: #CC775C;">
          <h1 class="text-6xl" style="margin-top: 40px;">MSCAtlas</h1>
        </div>
        <div
          class="bento col-span-4 h-48 rounded-3xl bg-white p-6 shadow-xl text-center hover:bg-base-200 transition seesee hover:shadow-2xl cursor-pointer"
          v-on:click="myaddRoute('document')"
          >
          <h1 class="text-4xl transition" style="margin-top: 50px;">Document</h1>
        </div>



        <div class="bento col-span-6 h-64 rounded-3xl bg-white p-6 shadow-xl transition hover:shadow-2xl">

          <h1 class="text-4xl">Browse Data</h1>
          <div class="grid grid-rows-2 grid-flow-col gap-4 h-36">
            <div class="card text-3xl shadow-xl card-bordered p-4 row-span-2 text-center transition hover:scale-105 cursor-pointer" style="background-color: #F0F0EB;"
                v-on:click="myaddRoute('dashboard')"
            >
              <span class="mt-8">Datasets</span>
            </div>

            <div class="card text-2xl  shadow-xl card-bordered p-4 row-span-1 text-center transition hover:scale-105 cursor-pointer" style="background-color: #F0F0EB;"
              v-on:click="myaddRoute('expression')"
            >
              Gene expression
            </div>
            <div class="card text-2xl  shadow-xl card-bordered p-4 row-span-1 text-center transition hover:scale-105 cursor-pointer" style="background-color: #F0F0EB;"
              v-on:click="myaddRoute('enrichment')"
            >
              Genesets ssGSEA
            </div>
          </div>
        </div>
        <div class="bento col-span-3 h-64 rounded-3xl bg-white shadow-xl transition hover:shadow-2xl">
          <div class="h-40 bg-clip-border bg-cover rounded-t-3xl bg-zinc-400"
            style="background-image: url('/classicGSEA-1.png')">
            <div class="hero-overlay rounded-t-3xl bg-opacity-60"></div>
          </div>
          <div class="text-center p-6">
            <h1 class="text-4xl">Visualization</h1>
          </div>


        </div>

        <div class="bento col-span-3 h-64 rounded-3xl bg-white p-6 shadow-xl transition hover:shadow-2xl">
          <h1 class="text-4xl">Statistics</h1>

          <div class="stat place-items-center font-sans">
            <div class="stat-title">Total</div>
            <div class="stat-value">2351</div>
            <div class="stat-desc">Samples</div>
          </div>

          
        </div>

      </div>

    </div>
  </div>



  <!-- Bento end -->

  <!-- Function start -->
  <div class="pt-4 pb-24" style="background-color: white;">

    <div class="min-w-screen-lg max-w-screen-2xl mx-auto">
      <h2 class="text-center text-3xl py-8">NEWLY UPDATE</h2>
      <a-row :gutter="20">
        <a-col v-for="i in 3" :key="i" :span="8">
          <div class="card shadow-xl" style="background-color: #F0F0EB;">

            <div class="card-body">
              <h2 class="card-title text-2xl font-serif">
                {{ functions[i - 1].title }}
              </h2>
              <!-- <p class="h-24">{{ functions[i - 1].description }}</p> -->
              <div class="card-actions justify-start">
                <span style="color: #91918d" class="text-lg font-serif">{{ functions[i - 1].date }}</span>
              </div>
            </div>
          </div>
        </a-col>
      </a-row>
    </div>


  </div>
</template>

<style scoped>
/* .bento:hover > h1 {
  transition: ease-in-out;
  transform: scale(1.2);
} */

.bento:hover {
  transform: scale(1.01)
    /* @apply shadow-2xl */
}

.seesee:hover h1 {
  transform: scale(1.25)
}

img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>

<script>

// import  html2canvas  from 'html2canvas';


export default {
  data() {
    return {

      currentStep: 2,
      functions: [
        { title: "Data updated", description: "Browser the data", date: "2023.12.15" },
        { title: "Version 1.0 released", description: "check the gene expression", date: "2023.11.29" },
        { title: "Add support for WikiPathway", description: "check the Patrhway activity", date: "2023.10.15" },
      ]
    }
  },
  mounted() {


    this.chart = new this.$Chart({
      container: 'functionbar',
      height: 200,
      width: 500
    })
    this.chart
      .interval()
      .data([
        { name: 'Tissue repair', value: 0.854 },
        { name: 'Adipogenesis', value: 0.770 },
        { name: 'Immunomodulation', value: 0.625 },
        { name: 'Anti-inflammatory', value: 0.496 },
        { name: 'Osteogenic', value: 0.472 },
        { name: 'Chondrogenesis', value: 0.113 },
        { name: 'Self-renewing', value: 0.023 },
       
      ])
      .encode('x', 'name')
      .encode('y', 'value')
      .coordinate({ transform: [{ type: 'transpose' }] })
      .encode('color', 'name')
      .scale('color', {
        type: 'ordinal',
        range: ["#8B4513", "#A0522D", "#CD853F", "#D2691E", "#8B7E66", "#C19A6B", "#B87333"]
      })
      .style('radiusTopLeft', 10)
      .style('radiusTopRight', 20)
      .style('radiusBottomRight', 30)
      .style('radiusBottomLeft', 40)
      .axis('x', { title: ''} )
      .axis('y', { title: ''} )
      .legend(false)
      .tooltip(false)

    this.chart.render();

  },
  methods: {
    myaddRoute(path) {
      // console.log(path)
      this.$router.push(path)
    },
    
  }
}
</script>