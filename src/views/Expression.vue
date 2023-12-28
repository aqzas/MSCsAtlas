<template>

<div class="container mx-auto" style="min-height: 80vh;">


    <div><a-input-search
            v-model:value="searchValue"
            placeholder="Input Gene Name (TP53)"
            size="large"
            @search="onSearch"
            @change="ErrorResponse = false"
            /></div>

    <a-spin v-show="onloading" tip="Loading...">
    <a-alert class="mt-16"
      message="Search in the database"
      description="The waiting time is approximately 5 seconds, depending on your network speed."
    ></a-alert>
</a-spin>

    <a-result v-show="ErrorResponse"
    class="mt-16"
    status="error" 
    title="No results found in database."
    sub-title="Please check you input. MSCAtlas only support seaching by GENE SYMBOL"
    />

    
    <Boxplot v-if="disPlayplot"
        :dat="total_data[ selectDemon ]"
        :xlabel="selectDemon"
        ylabel="Expression"
        customId="first"
        :itemName="ytitle"
    />

    <div class="mt-4" v-if="disPlayplot">
        <button class="btn btn-sm ml-1 first:ml-0"
        v-bind:class="{ 'btn-neutral': selectDemon == 'Source', 'bg-base-100': selectDemon != 'Source' }"
        @click="selectDemon = 'Source'"
        >Source
        </button>

        <button class="btn btn-sm ml-1"
            v-bind:class="{ 'btn-neutral': selectDemon == 'Treatment', 'bg-base-100': selectDemon != 'Treatment' }"
            @click="selectDemon = 'Treatment'"
        >Treatment
        </button>
        <button class="btn btn-sm ml-1"
            v-bind:class="{ 'btn-neutral': selectDemon == 'Disease', 'bg-base-100': selectDemon != 'Disease' }"
            @click="selectDemon = 'Disease'"
        >Disease
        </button>
    </div>

    <div class="h-64"></div>

</div>
      
</template>

<script>

import Boxplot from "../plot/Boxplot.vue"

export default {

    components: { Boxplot },

    data() {return {

        searchValue: "",
        selectDemon: '',
        ytitle: "",
        total_data: { },

        // Control
        disPlayplot: false,
        onloading: false,
        ErrorResponse: false
      

    }},
    methods: {
        onSearch() {
            this.onloading = true
            if( this.selectDemon == '') {
                this.selectDemon = "Source"
            }
            this.axios.get(`${this.$BasePath}/getGene/${this.searchValue}`)
                .then((response) => {
                    this.total_data = response.data
                    // console.log(this.total_data)
                    this.disPlayplot = true
                    this.ytitle = `${this.searchValue} vst z-score`
                    this.onloading = false
                })
                .catch((error) => {
                    this.onloading = false
                    this.ErrorResponse = true
                })
            
           
            // this.plot_data = this.total_data[ this.selectDemon ]
        }
    },
    mounted() {
  },
}
</script>