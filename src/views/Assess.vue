<template>
    <div class="container mx-auto">

        <a-upload-dragger v-model:fileList="fileList" name="file" :multiple="true"
            action="https://www.mocky.io/v2/5cc8019d300000980a055e76" @change="handleChange" @drop="handleDrop">
            <p class="ant-upload-drag-icon">
                <inbox-outlined></inbox-outlined>
            </p>
            <p class="ant-upload-text">Click or drag file to this area to upload</p>
            <p class="ant-upload-hint">
                Support for a single or bulk upload. Strictly prohibit from uploading company data or other
                band files
            </p>
        </a-upload-dragger>

        <div class="pt-4">
            <a-button type="primary" size="large" @click="handleClick">Assess</a-button>
        </div>

        <div id="haha" class="pt-4" v-show="visability"></div>


    </div>
</template>

<script>


export default {
    data() {
        return {
            fileList: [],

            visability: false,

            box_data: [
                { x: 'Differentiation ability', y: [1, 9, 16, 22, 24], z: 'Bone marrow' },
                { x: 'Differentiation ability', y: [2, 9, 14, 22, 21], z: 'Adipose' },
                { x: 'Immunomodulation', y: [1, 5, 8, 12, 16], z: 'Adipose' },
                { x: 'Immunomodulation', y: [3, 5, 7, 12, 14], z: 'Bone marrow' },
                { x: 'Secretory', y: [1, 8, 12, 19, 26], z: 'Adipose' },
                { x: 'Secretory', y: [5, 8, 12, 19, 21], z: 'Bone marrow' },
                { x: 'Antimicrobial', y: [2, 8, 12, 21, 28] , z: 'Adipose' },
                { x: 'Antimicrobial', y: [1, 8, 12, 15, 21] , z: 'Bone marrow'},
                { x: 'Angiogenesis', y: [1, 8, 14, 18, 24], z: 'Adipose' },
                { x: 'Angiogenesis', y: [7, 8, 14, 18, 29], z: 'Bone marrow' },
                { x: 'Protective', y: [3, 10, 17, 28, 30] , z: 'Adipose'},
                { x: 'Protective', y: [7, 10, 17, 20, 21] , z: 'Bone marrow' },
                { x: 'Apoptosis', y: [1, 7, 10, 17, 22] , z: 'Adipose'},
                { x: 'Apoptosis', y: [5, 7, 10, 17, 18] , z: 'Bone marrow'},
                { x: 'Immune regulation', y: [1, 6, 8, 13, 16] , z: 'Adipose'},
                { x: 'Immune regulation', y: [5, 6, 8, 10, 14] , z: 'Bone marrow'},
            ],
            radar_data: [
                { item: 'Differentiation ability', type: 'b', score: 17 },
                { item: 'Immunomodulation', type: 'b', score: 20 },
                { item: 'Secretory', type: 'b', score: 8 },
                { item: 'Antimicrobial', type: 'b', score: 9 },
                { item: 'Angiogenesis', type: 'a', score: 29 },
                { item: 'Protective', type: 'a', score: 21 },
                { item: 'Apoptosis', type: 'b', score: 9 },
                { item: 'Immune regulation', type: 'b', score: 16 },
            ],
        }
    },
    mounted() {
        this.init()
    },
    methods: {
        handleClick() {
            this.visability = true
        },
        init() {

            this.chart = new this.$Chart({
                container: 'haha',
            })

            this.chart.coordinate({ type: 'polar' });

            this.chart
                .box()
                .data(this.box_data)
                .encode('x', 'x')
                .encode('y', 'y')
                .encode('series', 'z')
                .encode('color', 'z')
                .scale('x', { paddingInner: 0.6, paddingOuter: 0.3 })
                .style('stroke', 'black')
                .axis('y', { tickCount: 5 })
               
            this.chart
                .data( this.radar_data )
                .area()
                .encode('x', 'item')
                .encode('y', 'score')
                .encode('shape', 'smooth')
                .style('fillOpacity', 0.5)
                .axis('y', { title: "" })
                // .scale('y', { domainMax: 80 });

            this.chart.render();

        }
    },


}

</script>