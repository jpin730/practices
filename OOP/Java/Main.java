class Main {
  public static void main(String[] args) {
    CarX carX = new CarX("AMQ123", new Account("Andres Herrera", "AND123"), "Chevrolet", "Sonic");
    // carX.passengers = 4;
    carX.setPassengers(4);
    carX.printDataCar();
  }
}