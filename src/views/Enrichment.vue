<template>
    <div class="container mx-auto">


        <div class="certain-category-search-wrapper" style="width: 250px">
            <a-auto-complete 
                v-model:value="searchValue" 
                class="certain-category-search"
                popup-class-name="certain-category-search-dropdown" 
                :dropdown-match-select-width="500" 
                style="width: 250px"
                :options="dataSource"
                @select="handleSearch">
                <template #option="item">
                    <template v-if="item.options">
                        <span>
                            {{ item.value }}
                        </span>
                    </template>
                    <template v-else>
                        <div style="display: flex; justify-content: space-between">
                            {{ item.value }}
                            <span>
                                <UserOutlined />
                            </span>
                        </div>
                    </template>
                </template>
                <a-input-search placeholder="input here" size="large"></a-input-search>
            </a-auto-complete>
        </div>

        <div class="pt-4"> <a-radio-group v-model:value="selectDemon" button-style="solid">

                <a-radio-button value="Source">Source</a-radio-button>
                <!-- <a-radio-button value="Marker">Marker</a-radio-button> -->
                <!-- <a-radio-button value="Condition">Condition</a-radio-button> -->
                <a-radio-button value="Treatment">Treatment</a-radio-button>
                <a-radio-button value="Disease">Disease</a-radio-button>

            </a-radio-group></div>

        <Boxplot v-if="disPlayplot" :dat="total_data[selectDemon]" :xlabel="selectDemon" ylabel="Expression"
            :itemName="searchValue" />

        <div></div>

    </div>
</template>

<style scoped>
.certain-category-search-dropdown .ant-select-dropdown-menu-item-group-title {
  color: #666;
  font-weight: bold;
}

.certain-category-search-dropdown .ant-select-dropdown-menu-item-group {
  border-bottom: 1px solid #f6f6f6;
}

.certain-category-search-dropdown .ant-select-dropdown-menu-item {
  padding-left: 16px;
}

.certain-category-search-dropdown .ant-select-dropdown-menu-item.show-all {
  text-align: center;
  cursor: default;
}

.certain-category-search-dropdown .ant-select-dropdown-menu {
  max-height: 300px;
}
</style>

<script>

import Boxplot from "../plot/Boxplot.vue"

export default {

    components: { Boxplot },

    data() {
        return {



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
            dataSource: [
                {
                    value: 'KEGG',
                    options: [
                        {
                            value: 'KEGG-1-12312',
                            
                        },
                        {
                            value: 'KEGG-2-12312',
                           
                        },
                    ],
                },
                {
                    value: 'GO',
                    options: [
                        {
                            value: 'GO-12-231',
                            
                        },
                        {
                            value: 'GO-12-231',
                        },
                    ],
                },
                {
                    value: 'Reactome',
                    options: [
                        {
                            value: 'RSA-1-23123',
                        },
                        {
                            value: 'RSA-1-23123',
                        },
                    ],
                },
            ],

            // Control
            disPlayplot: false


        }
    },
    methods: {
        handleSearch() {
            this.disPlayplot = true
            // this.plot_data = this.total_data[ this.selectDemon ]
        }
    }
}
</script>