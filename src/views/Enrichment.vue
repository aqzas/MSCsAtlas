<style scoped>
</style>

<template>
    <div class="container mx-auto" style="min-height: 80vh;">

        <a-form 
        :label-col="{ span: 4 }" 
        :wrapper-col="{ span: 8 }"
        name="basic" >

        <a-form-item label="Database">
            <a-select 
                v-model:value="database"
                placehoder="Select database"
                :options="databaseName.map(name => ({ value: name }))"
            ></a-select>
        </a-form-item>
        <a-form-item label="Geneset">
            <a-select 
                v-model:value="geneset"
                show-search
                :filter-option="filterOption"
                :options="genesets.map(name => ({ value: name }))"
            ></a-select>
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 4 }">
            <button class="btn bg-base-100 btn-sm" style="background-color: #CC775C" @click="handleSearch">Search</button>
            <button class="btn ml-4 btn-sm btn-active" @click="handleReset">Reset</button>
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 2 }">

            <Boxplot v-if="disPlayplot" 
                :dat="total_data[selectDemon]" 
                :xlabel="selectDemon" 
                ylabel="Expression"
                :itemName="geneset" 
                customId="second"
            />
        
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 4 }" v-if="disPlayplot">
            
            <button class="btn btn-sm ml-1 first:ml-0"
                v-bind:class="{ 'btn-neutral': selectDemon == 'Source', 'bg-base-100': selectDemon != 'Source' }"
                @click="selectDemon = 'Source'"
            >
                Source
            </button>
            <button class="btn btn-sm ml-1"
                v-bind:class="{ 'btn-neutral': selectDemon == 'Treatment', 'bg-base-100': selectDemon != 'Treatment' }"
                @click="selectDemon = 'Treatment'"
            >Treatment</button>
            <button class="btn btn-sm ml-1"
                v-bind:class="{ 'btn-neutral': selectDemon == 'Disease', 'bg-base-100': selectDemon != 'Disease' }"
                @click="selectDemon = 'Disease'"
            >Disease</button>
           
        </a-form-item>

        </a-form>

    </div>
</template>


<script>

import Boxplot from "../plot/Boxplot.vue"

export default {

    components: { Boxplot },

    data() {
        return {
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
            database: "KEGG_2021_Human",
            geneset: "ABC transporters",
            databaseName: [
               'KEGG_2021_Human', 'MAGNET_2023', 'MSigDB_Hallmark_2020', 'Reactome_2022', 'WikiPathways_2019_Human', 'GO_Biological_Process_2023'
            ],
            databaseData: {
                'KEGG_2021_Human': [ 'KEGG-1', 'KEGG-2' ],
                'MAGNET_2023': ['1', '2'],
                'GO': ['GO-1', 'GO-2'],
                'Reactome': ['Reactome-1', 'Reactome-2']
            },
            // Control
            disPlayplot: false
        }
    },
    mounted() {
        this.axios.get(`${this.$BasePath}/getDBname`)
            .then((response) =>{
                this.databaseData = response.data
            })
    },  
    computed: {
        genesets() {
            return this.databaseData[ this.database ]
        },
    },
    watch: {
        genesets(newV) {
            this.geneset = newV[0]
        }
    },
    methods: {
        handleSearch() {
            this.disPlayplot = true
           
            this.axios.get( `${this.$BasePath}/getPathway`, {
                params: {
                    db: this.database,
                    pathway: this.geneset
                }
            }).then((response) => {
                        this.total_data = response.data
                    })
            // this.plot_data = this.total_data[ this.selectDemon ]
        },
        handleReset() {
            this.disPlayplot = false
            this.database = "KEGG_2021_Human"
            this.geneset ="ABC transporters"

        },
        filterOption(input, option) {
            return option.value.toLowerCase().indexOf(input.toLowerCase()) >= 0;
        }
    }
}
</script>