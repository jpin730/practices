public class CarX extends Car {
  String brand;
  String model;

  public CarX(String license, Account driver, String brand, String model) {
    super(license, driver);
    this.brand = brand;
    this.model = model;
    // super. is parent
    // this. is child
  }

  // Polymorphism

  @Override
  void printDataCar() {
    super.printDataCar();
    System.out.println("Model: " + model + " Brand: " + brand);
  }
}