<template >
    <div class="min-h-screen flex container mx-auto">

        <!-- left menu -->
        <ul class="menu bg-white w-56 rounded-3xl ml-4 pt-6 text-base" style="height: 800px;">
            <li v-on:click="testValue('overview')"><a>Overview</a></li>
            <li class="pt-4" v-on:click="testValue('dataProces')"><a>Data Process</a></li>
            <li class="pt-4" v-on:click="testValue('Function')"><a>Function assay</a></li>
            <li class="pt-4" v-on:click="testValue('Browse')"><a>Browse data</a></li>
        </ul>

        <div class="bg-white rounded-3xl ml-4 p-6" style="height: 800px; width: 1200px">
           
            <article class="prose mx-auto text-lg" v-show="selectFlag == 'overview'">
                <h2>Overview</h2>
                <p>
                    MSCAtlas is an online platform for the analysis of mesenchymal stem cells, where users can upload their own data. MSCAtlas utilizes pre-defined functional gene sets and gene sets collected from public databases to conduct ssGSEA analysis on the samples. The resulting gene set scores can be used to assess the functionality of the samples, and also compared with a large number of public samples in MSCAtlas to obtain quantitative conclusions.
                </p>
            </article>
            <article class="prose mx-auto text-lg" v-show="selectFlag == 'dataProces'">
                <h2>Data Process</h2>
                <h3>Public data process</h3>
                <p>
                    All raw sequencing data in MSCAtlas are obtained from public databases such as SRA or ENA, and the information for each sample is manually annotated based on sample descriptions from SRA or GEO.
                </p>
                <p>
                    The raw data will undergo quality control using fastp, be aligned to the hg38 genome using STAR, and then counted using featureCount. The resulting raw count expression matrix will be transformed into TPM based on the gene length generated by featureCount, and the vst normalized values will be obtained using the method of DESeq2.
                </p>
            </article>
            <!--  -->
            <article class="prose mx-auto text-lg" v-show="selectFlag == 'Function'">
                <h2>Function</h2>
                <p>
                    The main function of MSCAtlas is to process expression data (in TPM format) of mesenchymal stem cell samples uploaded by users. The samples will undergo single-sample gene set enrichment analysis (ssGSEA) using predefined MSC functional gene sets and gene sets from major databases, and the results will be presented in the form of radar charts. Users can download these results as well as the visualized GSEA charts.
                </p>
            </article>
            <!--  -->
            <article class="prose mx-auto text-lg" v-show="selectFlag == 'Browse'">
                <h2>Browse data</h2>
                <p>
                    MSCAtlas also collects a large amount of public mesenchymal stem cell data, which has been manually annotated and organized, including information such as source, treatment, and disease. After processing, this data provides gene expression information and pathway activity information through ssGSEA analysis. Users can query and compare the expression/activity levels of specific genes/gene sets in different states.
                </p>
            </article>
        </div>


    </div>
</template>

<script>

export default {
    data() { 
        return {
            selectFlag: "overview",
        }
    },
    methods: {
        testValue(value) {
            this.selectFlag = value
        }
    }
}

</script>