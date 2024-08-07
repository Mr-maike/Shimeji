#include "DHT.h"
 
#define DHTPIN A1
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);
 
void setup() 
{
  Serial.begin(9600);
  Serial.println("DHT11 Teste!");
  dht.begin();
}
 
void loop() {

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(t) || isnan(h)) {
    Serial.println("Falha ao ler os dados do Sensor");
  }

  else{
    Serial.print("Umidade: ");
    Serial.print(h);
    Serial.print(" %t");
    Serial.print("Temperatura: ");
    Serial.print(t);
    Serial.println(" *C");
  }
}