
#include <AWS_IOT.h>
#include <WiFi.h>

#include "HX711.h"

#define snsr_clk 4
#define snsr_data 15

AWS_IOT hornbill;   // AWS_IOT instance

HX711 scale;

float currentweight, scale_factor;
float calibration_factor = -101525; // for me this vlaue works just perfect 419640

char WIFI_SSID[]="your Wifi SSID";
char WIFI_PASSWORD[]="Wifi Password";
char HOST_ADDRESS[]="AWS host address";
char CLIENT_ID[]= "client id";
char TOPIC_NAME[]= "your thing/topic name";

int status = WL_IDLE_STATUS;
int tick=0,msgCount=0,msgReceived = 0;
char payload[512];
char rcvdPayload[512];

void setup()
{
    Serial.begin(115200);
    delay(2000);

    while (status != WL_CONNECTED)
    {
        Serial.print("Attempting to connect to SSID: ");
        Serial.println(WIFI_SSID);
        // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
        status = WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

        // wait 5 seconds for connection:
        delay(5000);
    }
    
    Serial.println("Connected to wifi");

    if(hornbill.connect(HOST_ADDRESS,CLIENT_ID)== 0) // Connect to AWS using Host Address and Cliend ID
    {
        Serial.println("Connected to AWS");
        delay(1000);
    }
    else
    {
        Serial.println("AWS connection failed, Check the HOST Address");
        while(1);
    }

    delay(2000);
    
    scale.begin(snsr_data, snsr_clk);  //Initialize the 

    //scale.set_scale();           //for calibration
    scale.set_scale();       //measured scale factor
    scale.tare();       //Reset the scale to 0

    long zero_factor = scale.read_average(); //Get a baseline reading
    Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. 
    //Useful in permanent scale projects.

    Serial.println(zero_factor);
}

void loop()
{
  //For calibration purpose---------------------
  /*currentweight = scale.get_units();
  //Serial.print("Current weight:\t");
  //Serial.println(currentweight);
  Serial.print("Scale Factor:\t");
  Serial.println(scale_factor);*/
  //--------------------------------------------
  float h = scale.get_units();
  scale.set_scale(calibration_factor); //Adjust to this calibration factor 
  
  Serial.print("Reading: ");
  Serial.print(scale.get_units(), 3);
  Serial.print(" kg");
  //Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person
  Serial.print(" calibration_factor: ");
  Serial.print(calibration_factor);
  Serial.println();
  
  if(Serial.available())
  {
    char temp = Serial.read();
    if(temp == '+' || temp == 'a')
      calibration_factor += 10;
    else if(temp == '-' || temp == 'z')
      calibration_factor -= 10;
    else if(temp == 's')
      calibration_factor += 100;  
    else if(temp == 'x')
      calibration_factor -= 100;  
    else if(temp == 'd')
      calibration_factor += 1000;  
    else if(temp == 'c')
      calibration_factor -= 1000;
    else if(temp == 'f')
      calibration_factor += 10000;  
    else if(temp == 'v')
      calibration_factor -= 10000;  
    else if(temp == 't')
      scale.tare();  //Reset the scale to zero
  }
  
  if (isnan(h)){
      Serial.println("Failed to read from weight sensor!");
  }
  else
  {
      sprintf(payload,"Scale Factor: %f kg",h);
      
      if (hornbill.publish(TOPIC_NAME,payload) == 0)
      {
        Serial.print("Publish Message:"); 
        Serial.println(payload);
      }
      else
      {
        Serial.println("Publish failed");
      }
      
  }
  vTaskDelay(5000 / portTICK_RATE_MS);


  //To get value in kg---------------------
  //Serial.print("Get Unit:\t");
  //Serial.println((scale.get_units()));
  //----------------------------------------------
}
