//Mover [] movers = new Mover[10];
Planet earth; //single mover
Satellite moon;
Star sun;
PVector moon_location;
//Attractor a2;

void setup(){
  size(800,600);
   //single mover
  earth= new Planet(width/10,height+50,5.972);
  //a = new Attractor(30,0.25);
  sun = new Star(width/2,height/2,1.989);
  //for(int i = 0;i<movers.length;i++){
    //movers[i]=new Mover();
  //}
  //moon_location=earth.get_location();
  moon = new Satellite(width/12,height/12,7.347);
}

void draw(){
  background(255);
  sun.drag();
  sun.display();
  PVector SEforce=sun.attract_Earth(earth);
  PVector SMforce=sun.attract_Moon(moon);
  PVector EMforce=earth.attract_Moon(moon);
  earth.applyForce(SEforce);
  moon.applyForce(SMforce);
  moon.applyForce(EMforce);
  //each body needs to call the update and display method
  earth.update();
  earth.display();
  earth.checkEdges();
  moon.update();
  moon.display();
  moon.checkEdges();
  
  }

void mousePressed(){
  sun.clicked(mouseX,mouseY);
  
}

void mouseReleased(){
  sun.stopDragging();
  }