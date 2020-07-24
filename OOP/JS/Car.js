class Car {
  constructor(license, driver) {
    this.id;
    this.license = license;
    this.driver = driver;
    this.passengers;
  }
  printDataCar() {
    console.log(this.driver);
    console.log(this.driver.name);
    console.log(this.driver.document);
  }
}

 /* BEFORE ECMA 6
function Car(license, driver) {
  this.id;
  this.license = license;
  this.driver = driver;
  this.passengers;
}

Car.prototype.printDataCar = function () {
  console.log(this.driver);
  console.log(this.driver.name);
  console.log(this.driver.document);
} */