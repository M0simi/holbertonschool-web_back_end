/**
 * Returns a constant string about preferring const.
 * @returns {string} Message about const usage
 */
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

/**
 * Returns the ending part of the sentence.
 * @returns {string} A string " is okay"
 */
export function getLast() {
  return ' is okay';
}

/**
 * Returns a string that uses let and appends another message.
 * @returns {string} Combined message about let usage
 */
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
