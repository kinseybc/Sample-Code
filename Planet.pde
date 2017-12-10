class Planet{
  PVector location;
  PVector velocity;
  PVector acceleration;
  float mass;
  float gravity;
      
  Planet(int x, int y, float m){
    location=new PVector(x,y);
    velocity=new PVector(1,0);
    acceleration=new PVector(0,0);
    mass=m;
    gravity=6.67;
   
  }
  
PVector attract_Moon(Satellite s){
    PVector force = PVector.sub(location,s.location);
    float distance = force.mag();
    distance=constrain(distance,5,50);
    force.normalize();
    float strength = (gravity*mass*s.mass)/(distance*distance);
    force.mult(strength);
    return force;
  }
  
PVector get_location(){
  return location;
}

  
  void applyForce(PVector force){
    PVector f=PVector.div(force,mass);
    acceleration.add(f);
  }
  
  void update(){
    velocity.add(acceleration);
    location.add(velocity);
    acceleration.mult(0);
    
  }
  //PVector repulsive(Mover m){
    //PVector force = PVector.sub(location,m.location);
    //float distance = force.mag();
    //distance=constrain(distance,5,50);
    //force.normalize();
    //float strength = -1*((electroforce*mass*m.mass)/(distance*distance));
    //force.mult(strength);
    //return force;
  //}
  
  void display(){
    stroke(0);
    fill(127);
    strokeWeight(2);
    ellipse(location.x,location.y,12,12);
  }
  
  void checkEdges(){
    if(location.x>width){
      location.x=width;
      velocity.x=-velocity.x;
    }
    else if(location.x<0){
      location.x=0;
      velocity.x=-velocity.x;
    }
    if(location.y>height){
      velocity.y*=-1;
      location.y=height;
    }
    else if(location.y<0){
      location.y=0;
      velocity.y*=-1;
    }
  }

}