<template>
    <div>
        <div id="first"></div>
        <div id="second"></div>
    </div>
</template>

<script>

export default {
    name: 'boxplot',
    props: {
        dat: Array,
        xlabel: String,
        ylabel: String,
        itemName: String,
        customId: String
    },
    data() {
        return {
        }
    },  
    mounted() {
        this.init()
    },
    methods: {
        init() {
            let customId = this.customId
            this.chart = new this.$Chart({
                container: customId,
            })

            this.chart
                .box()
                .data(this.dat)
                .encode('x', this.xlabel)
                .encode('y', this.ylabel)
                .encode('color', this.xlabel)
                .scale('x', { paddingInner: 0.6, paddingOuter: 0.3 }) // box的宽度
                .scale('y', { zero: true })
                .style('stroke', 'black')
                .axis('y', { title: this.itemName })
                .axis('x', '')
                .tooltip(false)

            this.chart.render();
        },

        reredner() {
            this.chart.clear()

            this.chart
                .box()
                .data(this.dat)
                .encode('x', this.xlabel)
                .encode('y', this.ylabel)
                .encode('color', this.xlabel)
                .scale('x', { paddingInner: 0.6, paddingOuter: 0.3 }) // box的宽度
                .scale('y', { zero: true })
                .style('stroke', 'black')
                .axis('y', { title: this.itemName })
                .axis('x', '')
                .tooltip(false)

            this.chart.render();
        }
    },
    watch: {
        dat: function() {
            this.reredner()
        },

        itemName: function() {
            this.reredner()
        }

    }
}

</script>
