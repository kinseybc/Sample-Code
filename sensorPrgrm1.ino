//This programme will be for the sensor apparatus
//03 August 2016
//Successfully transmits both pair of data

//This is for the anemometer
#define inSig 4
int pulse;
int pulse1;
int count;
int rev;
unsigned long time1;
unsigned long time2;

int myNum[2];


//This section is for the magnet

#include<Wire.h>
#include<HMC5883L.h>

HMC5883L compass;

//variables for the XBee transmitter


void setup(){

//this acts as the power source for the sensor
pinMode(2,OUTPUT);
pinMode(3,OUTPUT);
digitalWrite(2,HIGH);
digitalWrite(3,HIGH);

//Power for XBee
pinMode(9,OUTPUT);
digitalWrite(9,HIGH);

pinMode(inSig,INPUT);

Serial.begin(9600);

while(!compass.begin()){
  Serial.println("Could not find the compass sensor!");
  delay(500);
}

delay(50);

   // Set measurement range
   compass.setRange(HMC5883L_RANGE_1_3GA);

   // Set measurement mode
   compass.setMeasurementMode(HMC5883L_CONTINOUS);

  // Set data rate
  compass.setDataRate(HMC5883L_DATARATE_30HZ);

  // Set number of samples averaged
  compass.setSamples(HMC5883L_SAMPLES_8);

  // Set calibration offset. See HMC5883L_calibration.ino
  compass.setOffset(0, 0);

delay(50);

}

void loop(){

//anemometer subroutine begins
time1=millis();
rev=revCount();
time2=millis();

int windSpeed = printSpeed(time1,time2,rev);

//Compass subRoutine begins

int azimuth=getHeading();

if(azimuth && windSpeed){

  myNum[0]=windSpeed;
  myNum[1]=azimuth;
}
//Section for transmitting Sensor System data
else if(!windSpeed){
  myNum[0]=0;
  }
else if(!azimuth){
  
  myNum[1]=0;
}
  
for(int i=0;i<2;i++){
  Serial.write(myNum[i]);
  }
delay(100);
}

//SubRoutines used in the loop section

int getHeading(){

Vector norm=compass.readNormalize();
float heading=atan2(norm.YAxis,norm.XAxis);
float declinationAngle=.2327;
heading += declinationAngle;

if(heading < 0){
  heading += 2*PI;
}

if(heading > 2*PI){
  heading -= 2*PI;
}

int azimuth = heading * 180/M_PI;

return azimuth;

}

int revCount(){
while(count<90){
  pulse=digitalRead(inSig);
  if(pulse!=pulse1){
    count=count+1;
    pulse1=pulse;
    }
  }
 int rev=1;
 count=0;
 return rev;
 }

int printSpeed(unsigned long time1, unsigned long time2, int rev){
  float deltime=(float)(time2-time1)/1000;
  int angVel=rev/deltime;
  //float windSpeed = 0.095*angVel + 0.86;
  return angVel;

}
