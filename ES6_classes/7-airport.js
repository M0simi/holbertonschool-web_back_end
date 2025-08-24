export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // override default toString method
  toString() {
    return `[object ${this._code}]`;
  }
}
