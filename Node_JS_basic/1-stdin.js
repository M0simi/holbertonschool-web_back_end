process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf-8');
// listen to the input of the user
process.stdin.on('data', (data) => {
  const name = process.stdout.read(); // trim remove any new line or spaces
  process.stdout.write(`Your name is: ${name}`);
});

// listen to the end of stdin
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
