var earthWeight = parseFloat(prompt('What is your weight?'));
var planet = 0;
while (planet !== 1 && planet !== 2) {
  planet = parseFloat(prompt('Choice your planet:\n1. Mars.\n2. Jupiter.'))
}

var gEarth = 9.8;
var g = [
  ['Mars', 3.7],
  ['Jupiter', 24.8]
]

marsWeight = earthWeight * g[planet-1][1] / gEarth;
marsWeight = marsWeight.toFixed(2);

document.write("Your weight in "+ g[planet-1][0] +" is <strong>" + marsWeight + " kg</strong>.");