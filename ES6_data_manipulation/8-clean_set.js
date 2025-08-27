export default function cleanSet(mySet, startString) {
  if (!startString) return '';

  return Array.from(mySet)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}
