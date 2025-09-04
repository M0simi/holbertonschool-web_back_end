const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');

    const database = process.argv[2]; // اسم الملف من arguments
    if (!database) {
      res.end('Cannot load the database');
      return;
    }

    fs.readFile(database, 'utf8', (err, data) => {
      if (err) {
        res.end('Cannot load the database');
        return;
      }

      const lines = data.trim().split('\n');
      lines.shift(); // نشيل الهيدر

      const students = {};
      let count = 0;

      for (const line of lines) {
        if (line.trim() === '') continue; // نتجاهل الأسطر الفاضية
        const [firstname, , , field] = line.split(',');
        if (!students[field]) students[field] = [];
        students[field].push(firstname);
        count++;
      }

      res.write(`Number of students: ${count}\n`);
      for (const field in students) {
        res.write(
          `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`,
        );
      }
      res.end();
    });
  } else {
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
