

class Star{
  PVector location;
  //PVector velocity;
  //PVector acceleration;
  float mass;
  float gravity;
  boolean dragging = false;
  PVector dragOffset;

  Star(int x, int y, float m){
    location = new PVector(x,y);
    mass = m;
    gravity = 6.67;
    dragOffset = new PVector(0.0,0.0);
  
  }
  
  PVector attract_Earth(Planet p){
    PVector force = PVector.sub(location,p.location);
    float distance = force.mag();
    distance = constrain(distance,5,50);
    force.normalize();
    float strength = (2*(gravity*mass*p.mass)/(distance*distance));
    force.mult(strength);
    return force;
  
  }
  
PVector attract_Moon(Satellite s){
    PVector force = PVector.sub(location,s.location);
    float distance = force.mag();
    distance=constrain(distance,5,50);
    force.normalize();
    float strength =((gravity*mass*s.mass)/(distance*distance));
    force.mult(strength);
    return force;
  }
  
  void display(){
    stroke(0);
    ellipseMode(CENTER);
    
    if(dragging) fill(50);
    else fill(175,200);
    ellipse(location.x,location.y,40,40);
  }
  
  void clicked(int mx, int my){
    float d = dist(mx,my,location.x,location.y);
    if(d<mass){
      dragging = true;
      dragOffset.x = location.x-mx;
      dragOffset.y = location.y-my;
    }
  
  }

  void stopDragging(){
    dragging=false;
  }
  void drag(){
    if(dragging){
      location.x = mouseX + dragOffset.x;
      location.y = mouseY + dragOffset.y;
    }
  
  }
}