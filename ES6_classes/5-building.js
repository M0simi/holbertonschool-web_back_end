export default class Building {
  constructor(sqft) {
    // save attribute
    this._sqft = sqft;

    // check if the current class is Bulding himself
    if (this.constructor !== Building &&
        this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // getter
  get sqft() {
    return this._sqft;
  }
}
