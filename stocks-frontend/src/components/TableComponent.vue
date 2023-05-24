<template>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Stock</th>
          <th>Cumulative Return</th>
          <th>Annualized Return</th>
          <th>Annualized Volatility</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="statistic in statistics" :key="statistic.name">
          <td>{{ statistic.name }}</td>
          <td>{{ statistic.cumulative_return }}</td>
          <td>{{ statistic.annualized_return }}</td>
          <td>{{ statistic.annualized_volatility }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
import { API_ENDPOINTS } from '@/api/api';

export default {
  data() {
    return {
      statistics: []
    }
  },
  mounted() {
    this.fetchStatistics();
    setInterval(this.fetchStatistics, 30 * 60 * 1000); // poll after 30 minutes
  },
  methods: {
    fetchStatistics() {
      const url = `${process.env.VUE_APP_BASE_URL}${API_ENDPOINTS.STATISTICS}`;
      axios.get(url)
        .then(response => {
          this.statistics = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
}
</script>

<style>
  .table-container {
    width: 100%;
    overflow-x: auto; 
  }
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    border: 1px solid #ccc;
    padding: 8px;
  }
  
  thead {
    background-color: #f2f2f2;
  }
  </style>

