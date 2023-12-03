<template>
    <div class="container mx-auto">

        <div><a-input-search v-model:value="searchValue" placeholder="input search text" enter-button="Search" size="large"
                @search="onSearch" /></div>
        <div id="haha"></div>

    </div>
</template>

<script>


export default {

    data() {
        return {
            dat: [
                { genre: 'Sports', sold: 275 },
                { genre: 'Strategy', sold: 115 },
                { genre: 'Action', sold: 120 },
                { genre: 'Shooter', sold: 350 },
                { genre: 'Other', sold: 150 },
            ],
            searchValue: "",
            selectDemon: 'Source',
        }
    },
    mounted() {
        this.init()
    },
    methods: {
        init() {

            this.chart = new this.$Chart({
                container: 'haha',
            })

            this.chart
                .interval() // 创建一个 Interval 标记
                .data(this.dat) // 绑定数据
                .encode('x', 'genre') // 编码 x 通道
                .encode('y', 'sold'); // 编码 y 通道

            this.chart.render();
        }
    }
}

</script>