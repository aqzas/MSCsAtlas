<template>

<div class="container mx-auto">


    <div><a-input-search
            v-model:value="searchValue"
            placeholder="Input Gene Name (TP53)"
            enter-button="Search"
            size="large"
            @search="onSearch"
            /></div>

    <div class="pt-4"> <a-radio-group v-model:value="selectDemon" button-style="solid">

        <a-radio-button value="Source">Source</a-radio-button>
        <!-- <a-radio-button value="Marker">Marker</a-radio-button> -->
        <!-- <a-radio-button value="Condition">Condition</a-radio-button> -->
        <a-radio-button value="Treatment">Treatment</a-radio-button>
        <a-radio-button value="Disease">Disease</a-radio-button>

    </a-radio-group></div>

    <Boxplot v-if="disPlayplot"
        :dat="total_data[ selectDemon ]"
        :xlabel="selectDemon"
        ylabel="Expression"
        :itemName="`${searchValue} expression (TPM)`"
    />

    <div></div>

</div>
      
</template>

<script>

import Boxplot from "../plot/Boxplot.vue"

export default {

    components: { Boxplot },

    data() {return {


            // { location: 'Oceania', Height: [1, 9, 16, 22, 24] },
            // { location: 'East Europe', Height: [1, 5, 8, 12, 16] },
            // { location: 'Australia', Height: [1, 8, 12, 19, 26] },
            // { location: 'South America', Height: [2, 8, 12, 21, 28] },
            // { location: 'North Africa', Height: [1, 8, 14, 18, 24] },
            // { location: 'North America', Height: [3, 10, 17, 28, 30] },
            // { location: 'West Europe', Height: [1, 7, 10, 17, 22] },
            // { location: 'West Africa', Height: [1, 6, 8, 13, 16] },
        searchValue: "",
        selectDemon: 'Source',
        total_data: {
            
            "Source": [
                { 'Source': "Bone marrow", "Expression": [5, 14, 21, 44, 6] },
                { 'Source': "Umbilical cord blood", "Expression": [1, 9, 16, 22, 24] },
                { 'Source': "Adipose", "Expression": [7, 23, 51, 61, 77] }
            ],
           
            "Treatment": [
                { 'Treatment': "Vrisu infect", "Expression": [3, 9, 51, 57, 81] },
                { 'Treatment': "2D culture", "Expression": [4, 9, 21, 33, 55] },
                { 'Treatment': "cultured with tooth epithelial cells", "Expression": [5, 9, 16, 22, 24] },
                { 'Treatment': "lentiviruses", "Expression": [6, 9, 16, 22, 24] }
            ],
            "Disease": [
                { 'Disease': "post-allogenic stem cell transplantation", "Expression": [8, 9, 17, 22, 42] },
                { 'Disease': "Rheumatoid Arthritis", "Expression": [9, 10, 16, 21, 77] },
                { 'Disease': "GVHD", "Expression": [11, 12, 16, 32, 45] }
            ],


        },
        // plot_data: "",

        // Control
        disPlayplot: false
      

    }},
    methods: {
        onSearch() {
            this.disPlayplot = true
            // this.plot_data = this.total_data[ this.selectDemon ]
        }
    }
}
</script>