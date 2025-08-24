// import class of Currency
import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    // check of currency type must be instance of Currency
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency object');
    }

    this._amount = amount;
    this._currency = currency;
  }

  // Getter & Setter for amount
  get amount() {
    return this._amount;
  }
  set amount(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = value;
  }

  // Getter & Setter for currency
  get currency() {
    return this._currency;
  }
  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new TypeError('Currency must be a Currency object');
    }
    this._currency = value;
  }

  // Method displayFullPrice
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Static method convertPrice
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}
