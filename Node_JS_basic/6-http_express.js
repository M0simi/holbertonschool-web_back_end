const express = require('express');

const app = express();

// لما يجي طلب على المسار الرئيسي "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// السيرفر يشتغل على البورت 1245
app.listen(1245);

module.exports = app;
