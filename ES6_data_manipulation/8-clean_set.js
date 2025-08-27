export default function cleanSet(mySet, startString) {
  return Array.from(mySet)
    .filter((value) => value.startsWith(startString) && startString.length > 0)
    .map((value) => value.slice(startString.length))
    .join('-');
}
