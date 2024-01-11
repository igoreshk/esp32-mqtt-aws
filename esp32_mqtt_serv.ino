// Import required libraries
#include "AWS_IOT.h"
#include "WiFi.h"

// Replace with your network credentials

AWS_IOT hornbill;   // AWS_IOT instance
const char* ssid ="***"; //Replace with your WiFi Name
const char* password ="***"; // Replace with your WiFi Password
char HOST_ADDRESS[]="endpoint.amazonaws.com"; //Replace with your AWS Custom endpoint Address

char CLIENT_ID[]= "Device-name";
char TOPIC_NAME[]= "topic";
int status = WL_IDLE_STATUS;
char payload[512];

int switchPIN = 7;  // pin switch
int switchStatus;   // status switch

void setup(){
  // Serial port for debugging purposes
  Serial.begin(115200);
  
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  
  Serial.println("Connected to wifi");
  
  // Print ESP32 Local IP Address
  Serial.println(WiFi.localIP());
  
  if(hornbill.connect(HOST_ADDRESS,CLIENT_ID)== 0) // Connect to AWS using Host Address and Client ID
    {
        Serial.println("Connected to AWS");
        delay(1000);
    }
    else
    {
        Serial.println("AWS connection failed, Check the HOST Address");
        while(1);
    }  
}

void loop() {
   switchStatus = digitalRead(switchPIN);   // read status of switch
   
   sprintf(payload,"{\"tracker_id\":\"1234567890\",\"longitude\":45.68838,\"latitude\":23.5543332,\"check_time\":\"2020-10-11T22:45:17.12722Z\",\"battery_level\":45}", switchStatus); // Create the payload for publishing
        
        if(hornbill.publish(TOPIC_NAME,payload) == 0)   // Publish the message (switchStatus)
        {        
            Serial.print("Publish Message:");   
            Serial.println(payload);
        }
        else
        {
            Serial.println("Publish failed");
        }
        // publish payload string every 1 minute .
        vTaskDelay(60000 / portTICK_RATE_MS);               

}
