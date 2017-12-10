class Satellite extends Planet{
  
  Satellite(int x, int y, float m){
    super(x,y,m); //this utilizes the initialization function of the parent class
  
  }
  void applyForce(PVector force){
    super.applyForce(force);
  }
  
  void display(){
    stroke(0);
    fill(127);
    strokeWeight(2);
    ellipse(location.x,location.y,5,5);
  }
  
}