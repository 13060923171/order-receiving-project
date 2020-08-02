#include "HX711.h"
/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>

#define snsr_clk 4
#define snsr_data 15

HX711 scale;
float currentweight, scale_factor;
float calibration_factor = 10000; //worked for my ** max scale setup 

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "YourAuthToken";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "YourNetworkName";
char pass[] = "YourPassword";

int status = WL_IDLE_STATUS;
float weight;

void setup()
{
    Serial.begin(115200);
    delay(2000);
    while (status != WL_CONNECTED)
    {
        Serial.print("Attempting to connect to SSID: ");
        Serial.println(ssid);
        // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
        status = WiFi.begin(ssid, pass);

        // wait 5 seconds for connection:
        delay(5000);
    } 
    Serial.println("Connected to wifi");
    
    scale.begin(snsr_data, snsr_clk);
    Blynk.begin(auth, ssid, pass);
    Serial.println("Connected to Blynk");

    //scale.set_scale();           //for calibration
    scale.set_scale();       //measured scale factor
    scale.tare();
    
}

void loop()
{
  Blynk.run();
  scale.set_scale(calibration_factor); //Adjust to this calibration factor

  weight = scale.get_units();

  Blynk.virtualWrite(V3, weight);
  delay(2000);
  //To get value in kg---------------------
  Serial.print("Reading: ");
  Serial.print(scale.get_units(), 3);
  Serial.print(" kg");
  //----------------------------------------------
}
