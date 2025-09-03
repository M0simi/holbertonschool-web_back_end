console.log('Welcome to Holberton School, what is your name?');

// listen to the input of the user
process.stdin.on('data', (data) => {
  const name = data.toString().trim(); // trim remove any new line or spaces
  console.log(`Your name is: ${name}`);
});

// listen to the end of stdin
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
