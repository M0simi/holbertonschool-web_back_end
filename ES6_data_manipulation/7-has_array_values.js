export default function hasValuesFromArray(set, array) {
    return array.every((elemeent) => set.has(element));
}
