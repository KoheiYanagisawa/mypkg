#include <WiFi.h>
#include <WiFiUdp.h>
#include <Servo.h>
#define led 2
Servo servo_1;
const char ssid[] = "your SSID"; // SSID
const char pass[] = "your password";  // password
const int localPort = 9000;
const IPAddress ip(192, 168, 11, 1);
const IPAddress subnet(255, 255, 255, 0);
WiFiUDP udp;
void setup() {
  servo_1.attach(5);
  pinMode(led, OUTPUT);
  Serial.begin(115200);
  WiFi.softAP(ssid, pass);
  delay(100);
  WiFi.softAPConfig(ip, ip, subnet);
  Serial.print("AP IP address: ");
  IPAddress myIP = WiFi.softAPIP();
  Serial.println(myIP);
  Serial.println("Starting UDP");
  udp.begin(localPort);  // UDP通信の開始(引数はポート番号)
  Serial.print("Local port: ");
  Serial.println(localPort);
}
void loop() {
  if (udp.parsePacket()) {
    int i = udp.read();
    Serial.println(i); // UDP通信で来た値を表示
    if(i == '0'){
      servo_1.write(0);
      digitalWrite(led, 0);
    }
    if(i == '1'){
      servo_1.write(120);
      digitalWrite(led, 1);
    }
  }
}
