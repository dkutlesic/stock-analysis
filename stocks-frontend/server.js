const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'dist')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

const host = '0.0.0.0' 
const port = process.env.PORT || 8080
app.listen(port, host)
console.log(`app is listening on port : ${port}`)