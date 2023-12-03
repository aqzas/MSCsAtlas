<template>

  <div class="container mx-auto"><a-card :hoverable="true">

   
    <a-form  
      :label-col="{ span: 2 }"
      name="basic"
    >
      <a-form-item label="Source">
        <a-select style="width: 200px" v-model:value="sourceSelect" :options="sourceOptions" mode="multiple"></a-select>
      </a-form-item>

      <a-form-item label="Treatment">
        <a-select style="width: 200px" v-model:value="treatmentSelect" :options="treatmentOptions" mode="multiple"></a-select>
      </a-form-item>

      <a-form-item label="Disease">
        <a-select style="width: 200px" v-model:value="diseaseSelect" :options="diseaseOptions" mode="multiple"></a-select>
      </a-form-item>

      <a-form-item label="Condition">
        <a-select style="width: 200px" v-model:value="conditionSelect" :options="conditionOptions" mode="multiple"></a-select>
      </a-form-item>

      <a-form-item :wrapper-col="{ offset: 2 } ">
        <a-button type="primary" html-type="submit">Submit</a-button>
      </a-form-item>
      
    </a-form>
  </a-card> </div>

  <div class="container mx-auto pt-4">
    <a-table
      :dataSource="dataSource" 
      :columns="columns"
      :loading="dataLoading"
    >

      <template #bodyCell="{ column, record }">
       
        <template v-if="['Source', 'Marker', 'Treatment', 'Condition', 'Species', 'SequencingType'].includes(column.key)">
            <a-tag
              v-for="tag in record[column.key]"
              :key="tag"
            >
            {{ tag }}
          </a-tag>
        </template>

      </template>
    </a-table>
  </div>
 
  
</template>


<script>
   export default {
    data() {
      return {
        dataSource: [
        ],

        dataLoading: true,

        columns: [
          {
            title: 'Dataset Id',
            dataIndex: 'ProjectId',
            key: 'ProjectId',
            witdh: 100
          },
          {
            title: 'Title',
            dataIndex: 'ProjectName',
            key: 'ProjectName',
            minWidth: 150,
            maxWidth: 200,
            resizable: true
          },
          {
            title: 'Source',
            dataIndex: 'Source',
            key: 'Source',
            witdh: 200
          },
          {
            title: 'Marker',
            dataIndex: 'Marker',
            key: 'Marker',
            witdh: 200
          },
          {
            title: 'Condition',
            dataIndex: 'Condition',
            key: 'Condition',
            ellipsis: true,
          },
          {
            title: 'Treatment',
            dataIndex: 'Treatment',
            key: 'Treatment',
            ellipsis: true,
          }, 
          {
            title: 'Sequencing Type',
            dataIndex: 'SequencingType',
            key: 'SequencingType',
            witdh: 150
          },
          {
            title: 'Species',
            dataIndex: 'Species',
            key: 'Species',
            witdh: 150
          }
        ],

        sourceSelect: [],
        sourceOptions: [
          { value: "Bone marrow" },
          { value: "Placenta" },
        ],

        treatmentSelect: [],
        treatmentOptions: [
          { value: "Gene Knock down"},
          { value: "Virus Infection"},
          { value: "3D Culture"}
        ],

        diseaseSelect: [],
        diseaseOptions: [
          { value: "Leukemia" },
          { value: "Obesity"}
        ],

        conditionSelect: [],
        conditionOptions: [
          { value: 'Adult'}, { value: 'Fetal' }
        ]

      };
    },

    mounted() {
      this.axios.get('https://www.frontierseeker.xyz/api/dashboard')
      .then((response) => {
        this.dataSource = response['data']['data']
        this.dataLoading = false
      })
    }
  };
</script>


