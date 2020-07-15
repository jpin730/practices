var villageArea = document.getElementById("village");
var canvas = villageArea.getContext("2d");

var tile = { url: "tile.png", load: false };
var cow = { url: "cow.png", load: false, x: randomBetween(0,420), y: randomBetween(0,420) };
var chicken = { url: "chicken.png", load: false, x: randomBetween(0,420), y: randomBetween(0,420) };
var pig = { url: "pig.png", load: false, x: randomBetween(0,420), y: randomBetween(0,420) };

tile.image = new Image();
tile.image.src = tile.url;
tile.image.addEventListener("load", loadTile);

cow.image = new Image();
cow.image.src = cow.url;
cow.image.addEventListener("load", loadCow);

chicken.image = new Image();
chicken.image.src = chicken.url;
chicken.image.addEventListener("load", loadChicken)

pig.image = new Image();
pig.image.src = pig.url;
pig.image.addEventListener("load", loadPig)

function loadTile() {
  tile.load = true;
  draw();
}

function loadCow() {
  cow.load = true;
  draw();
}

function loadChicken() {
  chicken.load = true;
  draw();
}

function loadPig() {
  pig.load = true;
  draw();
}

function draw() {
  if(tile.load) {
    canvas.drawImage(tile.image, 0, 0);    
  }
  if(cow.load) {
    canvas.drawImage(cow.image, cow.x, cow.y);    
  }
  if(chicken.load) {
    canvas.drawImage(chicken.image, chicken.x, chicken.y);    
  }
  if(pig.load) {
    canvas.drawImage(pig.image, pig.x, pig.y);    
  }
}

function randomBetween(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("keyup",moveAnimalWithArrow);

function moveAnimalWithArrow(keyEvent) {
  var animal = pig;
  var increment = 50;
  const key = {
    LEFT: 37,
    UP: 38,
    RIGHT: 39,
    DOWN: 40
  };
  if (animal.load) {
    switch (keyEvent.keyCode) {
      case key.LEFT:
        animal.x -= increment;
        break;
      case key.UP:
        animal.y -= increment;
        break;
      case key.RIGHT:
        animal.x += increment;
        break;
      case key.DOWN:
        animal.y += increment;
        break;
      default:
        break;
    }
    draw();
  }
}