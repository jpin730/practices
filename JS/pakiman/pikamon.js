class Pikamon {
  constructor(name, hp, attack) {
    this.image = new Image();
    this.name = name;
    this.hp = hp;
    this.attack = attack;
    this.image.src = images[this.name];
  }
  talk() {
    alert(this.name);
  }
  display() {
    document.body.appendChild(this.image);
    document.write("<p>")
    document.write("<strong>" + this.name + "</strong><br>")
    document.write("HP: " + this.hp + "<br>")
    document.write("Attack: " + this.attack)
    document.write("</p>")
    document.write("<hr>")
  }
}