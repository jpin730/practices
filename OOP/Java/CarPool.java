public class CarPool extends Car {
  String brand;
  String model;

  public CarPool(String license, Account driver, String brand, String model) {
      super(license, driver);
      this.brand = brand;
      this.model = model;
  }
}