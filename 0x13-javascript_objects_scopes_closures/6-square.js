class CharSquare extends Square {
  charPrint(c) {
    if (this.width && this.height) {
      const char = c === undefined ? 'X' : c;
      for (let i = 0; i < this.height; i++) {
        console.log(char.repeat(this.width));
      }
    } else {
      console.log("Empty square");
    }
  }
}
