import { readDatabase } from '../utils.js';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const file = process.argv[2];
      const students = await readDatabase(file);
      let output = 'This is the list of our students\n';
      const sortedFields = Object.keys(students).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase())
      );
      sortedFields.forEach(field => {
        output += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
      });
      res.status(200).send(output.trim());
    } catch (err) {
      res.status(500).send(err.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    try {
      const major = req.params.major;
      if (major !== 'CS' && major !== 'SWE') {
        return res.status(500).send('Major parameter must be CS or SWE');
      }
      const file = process.argv[2];
      const students = await readDatabase(file);
      if (!students[major]) return res.status(200).send('List:');
      res.status(200).send(`List: ${students[major].join(', ')}`);
    } catch (err) {
      res.status(500).send(err.message);
    }
  }
}

export default StudentsController;
