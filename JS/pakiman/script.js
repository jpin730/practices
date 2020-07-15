var c = console.log;

var images = [];
images["Cowamon"] = "cow.png";
images["Chickon"] = "chicken.png";
images["Pigon"] = "pig.png";

// var cowamon = new Pikamon("Cowamon", 100, 30);
// var chickon = new Pikamon("Chickon", 80, 50);
// var pigon = new Pikamon("Pigon", 120, 40);

var pikadex = [];
pikadex.push(new Pikamon("Cowamon", 100, 30));
pikadex.push(new Pikamon("Chickon", 80, 50));
pikadex.push(new Pikamon("Pigon", 120, 40));

for (var pikamon of pikadex) {
  pikamon.display();
}