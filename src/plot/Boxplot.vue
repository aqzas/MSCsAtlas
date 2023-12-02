<template>
    <div>
        <div id="boxplot"></div>
    </div>
</template>

<script>

export default {
    name: 'boxplot',
    props: {
        dat: Array,
        xlabel: String,
        ylabel: String,
        height: {
                type: Number,
                default: 520
        }
    },
    data() {
        return {
            chart: null
        }
    },  
    mounted() {
        this.init()
    },
    methods: {
        init() {
            this.chart = new this.$Chart({
                container: 'boxplot',
                height: this.height,
                autoFit: true
            })

            this.chart
                .box()
                .data(this.dat)
                .encode('x', this.xlabel)
                .encode('y', this.ylabel)
                .encode('color', 'x')
                .scale('x', { paddingInner: 0.6, paddingOuter: 0.3 })
                .scale('y', { zero: true })
                .style('stroke', 'black')
                .tooltip(false)

            this.chart.render();
        }
    },
    watch: {
        dat: function() {

            this.chart
                .data(dat)
                .encode('x', this.xlabel)
                .encode('y', this.ylabel)
            
            this.chart.render()

        }
    }
}

</script>
