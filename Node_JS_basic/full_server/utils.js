import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) return reject(new Error('Cannot load the database'));
      const lines = data.split('\n').filter(line => line.trim() !== '');
      const students = {};
      lines.slice(1).forEach(line => {
        const [firstname, , field] = line.split(',');
        if (!students[field]) students[field] = [];
        students[field].push(firstname);
      });
      resolve(students);
    });
  });
}
