<template>
    <div class="container mx-auto pb-4" style="min-height: 90vh;">

        <a-upload-dragger v-model:fileList="fileList" name="file" :max-count="1" @change="handleChange"
            :action="uploadPath">
            <p class="ant-upload-drag-icon">
                <!-- <inbox-outlined></inbox-outlined> -->
            </p>
            <p class="ant-upload-text">Click or drag file to this area to upload</p>
            <p class="ant-upload-hint">
                Support for gene expression with TPM unit in CSV formant. Strictly prohibit from uploading unrelated data or other
                band files.
            </p>
        </a-upload-dragger>

        <button class="btn btn-xl mt-2 btn-warning" @click="downloadSample">Download sample file</button>
        <button class="btn btn-xl mt-2 ml-4 btn-active " @click="">Reset</button>
        <Transition>
                <button class="btn btn-xl ml-4 btn-success" @click="handleClick" v-show="ableAssess">Assess funtion</button>
        </Transition>
       

       

        <div class="flex mx-auto" v-show="visability" >
            <Transition>
                <div id="haha" class="pt-4"></div>
            </Transition>
            <Transition>
                <a-table :dataSource="radar_data" :columns="columns" :pagination="false" />
            </Transition>
        </div>

        <div class="pt-4">
            <Transition>
                <button class="btn btn-xl mt-2 bg-white" v-show="visability" @click="downFig">Save figure</button>
            </Transition>
        </div>



    </div>
</template>

<style scoped>
</style>

<script>

import "../assets/html2canvas"


export default {
    data() {
        return {
            fileList: [],
            visability: false,
            uploadPath: `${this.$BasePath}/uploadexp`,
            readFlag: false,

            columns: [
                {
                    title: "Term",
                    dataIndex: 'Term',
                    key: 'Term'
                },
                {
                    title: "NES",
                    dataIndex: 'NES',
                    key: "NES"
                }

            ],
            box_data: [
                { x: 'Differentiation ability', y: [1, 9, 16, 22, 24], z: 'Bone marrow' },
                { x: 'Differentiation ability', y: [2, 9, 14, 22, 21], z: 'Adipose' },
                { x: 'Immunomodulation', y: [1, 5, 8, 12, 16], z: 'Adipose' },
                { x: 'Immunomodulation', y: [3, 5, 7, 12, 14], z: 'Bone marrow' },
            ],
            radar_data: [
                { Term: 'Differentiation ability', type: 'b', NES: 17 },
                { Term: 'Immunomodulation', type: 'b', NES: 20 },
            ],
        }
    },
    computed: {
        ableAssess() {
            return this.fileList.length > 0 && this.readFlag
        },
    },
    methods: {

        downloadSample() {
            const filePath = "/sample.tpm.csv";

            // 创建一个隐藏的a标签
            const link = document.createElement("a");
            link.href = filePath;
            link.download = "test.Sample.csv"; // 下载时的文件名
            document.body.appendChild(link);

            // 模拟点击a标签来触发下载
            link.click();
            document.body.removeChild(link);

        },

        downFig() {

            const ins = document.getElementById("haha")

            html2canvas(ins, {
                useCORS: true,
                scale: 2,
            }).then(canvas => {
                const imgData = canvas.toDataURL('image/jpg', 2.0);
                
                const link = document.createElement("a");
                link.href = imgData;
                link.download = 'assess.jpg';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            });


        },

        handleClick() {
            this.visability = true
        },
        handleChange(info) {
            this.readFlag = false
            if (info.file.status == 'done') {
                this.box_data = info.fileList[0].response['background']
                this.radar_data = info.fileList[0].response['data']
                this.init()
                this.readFlag = true
            }
        },
        // Plot function
        init() {

            this.chart = new this.$Chart({
                container: 'haha',
            })

            this.chart.coordinate({ type: 'polar' });

            this.chart
                .data(this.radar_data)
                .area()
                .encode('x', 'Term')
                .encode('y', 'NES')
                .encode('shape', 'smooth')
                .style('fillOpacity', 0.5)
                .axis('y', { title: "" })

            this.chart
                .box()
                .data(this.box_data)
                .encode('x', 'x')
                .encode('y', 'y')
                // .encode('series', 'z')
                // .encode('color', 'z')
                //TODO(chensy) Change the style here.
                .scale('x', { paddingInner: 0.6, paddingOuter: 0.3 })
                // .scale('y', {
                //     type: 'linear',
                //     range: [0, 1]
                //  })
                .style('stroke', 'black')
                .tooltip(false)


            // .scale('y', { domainMax: 80 });

            this.chart.render();

        }
    },


}

</script>