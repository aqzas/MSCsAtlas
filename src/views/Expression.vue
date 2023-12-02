<template>

<div class="container mx-auto">


    <div><a-input-search
            v-model:value="searchValue"
            placeholder="input search text"
            enter-button="Search"
            size="large"
            @search="onSearch"
            /></div>

    <div class="pt-4"> <a-radio-group v-model:value="selectDemon" button-style="solid">

        <a-radio-button value="Source">Source</a-radio-button>
        <a-radio-button value="Marker">Marker</a-radio-button>
        <a-radio-button value="Condition">Condition</a-radio-button>
        <a-radio-button value="Treatment">Treatment</a-radio-button>
        <a-radio-button value="Disease">Disease</a-radio-button>

    </a-radio-group></div>


    <div>

        Hello, {{ $route.params.way }}. {{  selectDemon }}

    </div>

    <Boxplot 
        :dat="plot_data"
        xlabel="x"
        ylabel="y"
    />

    <div></div>
    

</div>
      
</template>

<script>

import Boxplot from "../plot/Boxplot.vue"

export default {

    components: { Boxplot },

    data() {return {

        searchValue: "",
        selectDemon: 'Source',
        chart: null,

        plot_data: [
            { x: 'Oceania', y: [1, 9, 16, 22, 24] },
            { x: 'East Europe', y: [1, 5, 8, 12, 16] },
            { x: 'Australia', y: [1, 8, 12, 19, 26] },
            { x: 'South America', y: [2, 8, 12, 21, 28] },
            { x: 'North Africa', y: [1, 8, 14, 18, 24] },
            { x: 'North America', y: [3, 10, 17, 28, 30] },
            { x: 'West Europe', y: [1, 7, 10, 17, 22] },
            { x: 'West Africa', y: [1, 6, 8, 13, 16] },
        ]
      

    }},
}
</script>