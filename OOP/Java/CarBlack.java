import java.util.ArrayList;
import java.util.Map;

public class CarBlack extends Car {
  Map< String, Map<String, Integer> > typeCarAccepted;
  ArrayList<String> seatsMaterial;

  public CarBlack(String license, Account driver, Map<String,Map<String,Integer>> typeCarAccepted, ArrayList<String> seatsMaterial) {
    super(license, driver);
    this.typeCarAccepted = typeCarAccepted;
    this.seatsMaterial = seatsMaterial;
  }
}