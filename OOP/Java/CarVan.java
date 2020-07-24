import java.util.ArrayList;
import java.util.Map;

public class CarVan extends Car {
  Map< String, Map<String, Integer> > typeCarAccepted;
  ArrayList<String> seatsMaterial;

  public CarVan(String license, Account driver, Map<String, Map<String, Integer>> typeCarAccepted,
      ArrayList<String> seatsMaterial) {
    super(license, driver);
    this.typeCarAccepted = typeCarAccepted;
    this.seatsMaterial = seatsMaterial;
  }

  // Polymorphism

  @Override
  public void setPassengers(Integer passengers) {
    if (passengers == 6) {
      this.passengers = passengers;
    }
    else {
      System.out.println("Correct passengers value is 6.");
    }
  }
}