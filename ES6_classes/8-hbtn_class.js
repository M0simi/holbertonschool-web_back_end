export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // convert to class Number
  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return this._size;     // Number(hc)
    if (hint === 'string') return this._location; // String(hc)
    return this._size;                             // the defult
  }
}
