<template>
  <div class="container mx-auto"><a-card :hoverable="true" class="shadow-xl rounded-3xl">

      <a-form  name="basic" :label-col="{ style: { width: '100px' } }">
        <a-row :gutter="24">
          <a-col :span="12">
            <a-form-item label="Dataset Id">
              <a-select v-model:value="projectSelect" :options="projectOptions" mode="multiple"></a-select>
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="Source">
              <a-select v-model:value="sourceSelect" :options="sourceOptions" mode="multiple"></a-select>
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="Treatment">
              <a-select v-model:value="treatmentSelect" :options="treatmentOptions" mode="multiple"></a-select>
            </a-form-item>
          </a-col>
          <a-col :span="12">
            <a-form-item label="Disease">
              <a-select v-model:value="diseaseSelect" :options="diseaseOptions" mode="multiple"></a-select>
            </a-form-item>
          </a-col>
        </a-row>

      </a-form>

      <button style="margin-left: 100px; background-color: #CC775C" class="btn font-serif" @click="handleSearch">Search</button>
      <button class="btn ml-4 btn-active font-serif" @click="handleCancel">Reset</button>
    </a-card> 
  </div>

  <div class="container mx-auto pt-4">
    <a-table :dataSource="dataView" :columns="columns" :loading="dataLoading" :scroll="{ x: 1200 }">

      <template #bodyCell="{ column, record }">

        <template v-if="['Source', 'Marker', 'Treatment', 'Condition', 'Species', 'SequencingType', 'Disease'].includes(column.key)">
          <a-tag v-for="tag in record[column.key]" :key="tag">
            {{ tag }}
          </a-tag>
        </template>

      </template>
      <template #expandedRowRender="{ record }">
        <p class="font-bold">Summary: </p>
        <p style="margin: 0">
          {{ record.Summary.replace(/ Less\.\.\.$/, '') }}
        </p>
      </template>

    </a-table>
    
    <button class="btn btn-xl mt-2 mb-2 bg-white" style="float: right" @click="downloadCSV( convertToCSV(dataView) )">Download table</button>

  </div>
</template>


<script>
export default {
  data() {
    return {
      dataSource: [
      ],

      dataView: [],

      dataLoading: true,

      columns: [
        {
          title: 'Dataset Id',
          dataIndex: 'ProjectId',
          key: 'ProjectId',
          width: 130,
          fixed: 'left'

        },
        {
          title: 'Title',
          dataIndex: 'ProjectName',
          key: 'ProjectName',
          width: 400,
          fixed: 'left'

        },
        // {
        //   title: 'Marker',
        //   dataIndex: 'Marker',
        //   key: 'Marker',

        // },
       
        {
          title: 'Treatment',
          dataIndex: 'Treatment',
          key: 'Treatment',
          ellipsis: true,
        },
        {
          title: 'Source',
          dataIndex: 'Source',
          key: 'Source',

        },
        {
          title: 'Disease',
          dataIndex: 'Disease',
          key: 'Disease',
          ellipsis: true,
        }
      ],


      projectSelect: [],
      projectOptions: [

      ],

      sourceSelect: [],
      sourceOptions: [
        { value: "Bone marrow" },
        { value: "Placenta" },
      ],

      treatmentSelect: [],
      treatmentOptions: [
        { value: "Gene Knock down" },
        { value: "Virus Infection" },
        { value: "3D Culture" }
      ],

      diseaseSelect: [],
      diseaseOptions: [
        { value: "Leukemia" },
        { value: "Obesity" }
      ],

      // conditionSelect: [],
      // conditionOptions: [
      //   { value: 'Adult' }, { value: 'Fetal' }
      // ]

    };
  },

  mounted() {
    this.axios.get(`${this.$BasePath}/dashboard`)
      .then((response) => {
        this.dataSource = response['data']['data']
        this.dataView = this.dataSource
        this.dataLoading = false
        this.projectOptions = this.dataSource.map(item => ({ value: item.ProjectId }))

        this.sourceOptions = [...new Set(this.dataSource.flatMap(item => item.Source ? item.Source : []).filter(value => value !== null))].map(item => ({ value: item }))
        this.treatmentOptions = [...new Set(this.dataSource.flatMap(item => item.Treatment ? item.Treatment : []).filter(value => value !== null))].map(item => ({ value: item }))
        this.diseaseOptions = [...new Set(this.dataSource.flatMap(item => item.Disease ? item.Disease : []).filter(value => value !== null))].map(item => ({ value: item }))

      })
  },
  methods: {

    convertToCSV(objArray) {
      var jsonData = JSON.stringify(objArray)
      return jsonData
    },

    downloadCSV(csv) {
      var blob = new Blob([csv], { type: 'application/json' });
      var url = window.URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'data.json';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    },


    handleSearch() {

      this.dataView = this.dataSource
      console.log(this.dataView)
      if (this.projectSelect.length > 0) {
        this.dataView = this.dataView.filter(item => (this.projectSelect.includes(item.ProjectId)))
      }

      if (this.sourceSelect.length > 0) {
        // this.dataView = this.dataView.filter(item => (this.sourceSelect.some(sel => (item.Source.include(sel)))))
        this.dataView = this.dataView.filter((item) => {
          if ( item.Source === undefined ) {
            return false
          }
          let ins = (typeof item.Source === 'string') ? [ item.Source ] : item.Source;
          return this.sourceSelect.some( sel => ins.includes(sel) )
        })
        console.log("Source")
      }

      if (this.treatmentSelect.length > 0) {
        
        this.dataView = this.dataView.filter((item) => {
          if ( item.Treatment === undefined ) {
            return false
          }
          let ins = ( typeof item.Treatment === 'string') ? [ item.Treatment ] : item.Treatment;
          return this.treatmentSelect.some( sel => ins.includes(sel) )
        })
      }

      if (this.diseaseSelect.length > 0) {
        

        this.dataView = this.dataView.filter((item) => {
          if ( item.Disease === undefined ) {
            return false
          }
          let ins = (typeof item.Disease === 'string') ? [ item.Disease ] : item.Disease;
          return this.diseaseSelect.some( sel => ins.includes(sel) )
        })
      }
    },
    handleCancel() {
      this.dataView = this.dataSource
      this.sourceSelect = []
      this.projectSelect = []
      this.treatmentSelect = []
      this.diseaseSelect = []
      this.conditionSelect = []
    }

  }
};
</script>


