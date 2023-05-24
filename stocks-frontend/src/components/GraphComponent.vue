<template>
  <div>
    <div ref="plotly"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Plotly from 'plotly.js-dist';

import { API_ENDPOINTS } from '@/api/api';

export default {
  data() {
    return {
      stocksData: [],
      layout: {
        title: 'Stock values',
        xaxis: {
          title: 'Date'
        },
        yaxis: {
          title: 'Value'
        }
      }
    };
  },
  mounted() {
    this.fetchStocksData();
    setInterval(this.fetchStocksData, 30 * 60 * 1000); // poll after 30 minutes
  },
  methods: {
    fetchStocksData() {
      const url = `${process.env.VUE_APP_BASE_URL}${API_ENDPOINTS.GRAPH}`;
      axios
        .get(url)
        .then(response => {
          const stocks = response.data;
          const stockNames = new Set(stocks.map(stock => stock.name));
          this.stocksData = []; // clear previous data
          stockNames.forEach(name => {
            const data = stocks.filter(stock => stock.name === name);
            this.stocksData.push({
              name: name,
              data: data
            });
          });
          this.plotChart();
        })
        .catch(error => {
          console.log(error);
        });
    },
    plotChart() {
      const colorblindColors = ['#d55e00', '#0072b2', '#f0e442', '#cc79a7', '#009e73'];
      const traces = [];
      this.stocksData.forEach((stock,i) => {
        traces.push({
          x: stock.data.map(stock => stock.date),
          y: stock.data.map(stock => stock.normalized_value),
          mode: 'lines',
          line: { color: colorblindColors[i % colorblindColors.length] },
          name: stock.name
        });
      });
      Plotly.newPlot(this.$refs.plotly, traces, this.layout);
    }
  }
};
</script>
