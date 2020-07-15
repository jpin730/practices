const c = console.log;

class Banknote {
  constructor(denomination, quantity) {
    this.denomination = denomination;
    this.quantity = quantity;
  }
}

function withdrawCash() {
  requestedCash = parseInt(document.getElementById("requestedCash").value);
  deliveredCash = [];
  for (const banknote of atm) {
    if (requestedCash > 0) {
      banknoteToDeliver = Math.floor(requestedCash/banknote.denomination);
      if (banknoteToDeliver > banknote.quantity) {
        banknoteDelivered = banknote.quantity;
      }
      else {
        banknoteDelivered = banknoteToDeliver;
      }
      deliveredCash.push(new Banknote(banknote.denomination, banknoteDelivered));
      requestedCash -= banknoteDelivered * banknote.denomination;
    }
  }
  if (requestedCash > 0) {
    resultDiv.innerHTML = "Cash can't be delivered :(";
  }
  else {
    resultDiv.innerHTML = "";
    for (const banknote of deliveredCash) {
      if (banknote.quantity) {
        resultDiv.innerHTML += banknote.quantity + "x $" + banknote.denomination.toFixed(2) + "<br>";
      }
    }
    c(deliveredCash);
  }
}

var atm = [];
atm.push(new Banknote(100, 5));
atm.push(new Banknote(50, 10));
atm.push(new Banknote(20, 5));
atm.push(new Banknote(10, 10));
atm.push(new Banknote(5, 5));
var requestedCash = 0;
var deliveredCash = [];
var banknoteToDeliver = 0;
var banknoteDelivered = 0;

var resultDiv = document.getElementById("resultDiv");
var withdraw = document.getElementById("withdraw");
withdraw.addEventListener("click", withdrawCash);