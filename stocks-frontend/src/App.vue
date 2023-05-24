<template>
  <div class="container">
    <h1 class="title">Real-Time Stock Values and Statistics</h1>
    <p class="description">Welcome to the stock analysis page 
      where you can explore real-time stock values and compare their statistics.</p>
    <GraphComponent />
    <TableComponent />
  </div>
</template>

<script>
import GraphComponent from './components/GraphComponent.vue'
import TableComponent from './components/TableComponent.vue'

export default {
 name: 'App',
 components: {
  GraphComponent,
  TableComponent
 }
}
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  font-size: 28px;
  margin-bottom: 20px;
}

.description {
  font-size: 18px;
  margin-bottom: 30px;
  color: #555;
}

#app {
 font-family: Avenir, Helvetica, Arial, sans-serif;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale;
 text-align: center;
 color: #2c3e50;
 margin-top: 60px;
}
</style>
