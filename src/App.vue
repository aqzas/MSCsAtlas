<template>
  <div>
    <a-table :dataSource="dataSource" :columns="columns">
      <template #bodyCell="{ column, record }">
        <template v-if="['Source', 'Marker', 'Treatment', 'Condition'].includes(column.key)">
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

        columns: [
          {
            title: 'Dataset Id',
            dataIndex: 'ProjectId',
            key: 'ProjectId',
          },
          {
            title: 'Title',
            dataIndex: 'ProjectName',
            key: 'ProjectName',
          },
          {
            title: 'Source',
            dataIndex: 'Source',
            key: 'Source',
          },
          {
            title: 'Marker',
            dataIndex: 'Marker',
            key: 'Marker',
          },
          {
            title: 'Condition',
            dataIndex: 'Condition',
            key: 'Condition',
          },
          {
            title: 'Treatment',
            dataIndex: 'Treatment',
            key: 'Treatment',
          },
        ],
      };
    },

    mounted() {
      this.axios.get('https://www.frontierseeker.xyz/api/dashboard')
      .then((response) => {
        this.dataSource = response['data']['data']
        console.log(response['data']['data'])
      })
    }
  };
</script>


