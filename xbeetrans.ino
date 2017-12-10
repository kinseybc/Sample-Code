//this code will go to the receiver module

byte prBts[2];
byte inByte;
int pr1;
int pr2;
int index=0;


void setup(){
  
Serial.begin(9600);
//pinMode(7,OUTPUT);
//pinMode(8,OUTPUT);
//pinMode(9,OUTPUT);

}

void loop(){

if(Serial.available()>0){
  //inByte=Serial.read();
  //prBts[index]=inByte;
  //index++;
  prBts[0]=Serial.read();
  prBts[1]=Serial.read();
}
//Serial.flush();
//index=0;

for(int i=0;i<2;i++){
  
  Serial.print(prBts[i]);

}

Serial.println(" ");

//pr1=int(prBts[0]);
//pr2=int(prBts[1]);

//if(pr1==0 && pr2==0){
  //digitalWrite(7,HIGH);
  //delay(750);
  //digitalWrite(7,LOW);
//}

//else if(pr1==1 && pr2==0){
  //digitalWrite(8,HIGH);
  //delay(750);
  //digitalWrite(8,LOW);
//}

//else if(pr1==0 && pr2==1){
  //digitalWrite(9,HIGH);
  //delay(750);
  //digitalWrite(9,LOW);
//}

//else if(pr1==1 && pr2==1){
  //digitalWrite(7,HIGH);
  //digitalWrite(8,HIGH);
  //digitalWrite(9,HIGH);
  //delay(750);
  //digitalWrite(7,LOW);
  //digitalWrite(8,LOW);
  //digitalWrite(9,LOW);
//}

delay(100);
}
