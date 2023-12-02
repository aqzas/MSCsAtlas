<template>
  <div>
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


