#define LEDPIN 11
#define BUZZER 14
void setup() {
// Setup serial for monitor and Setup Serial1 for BlueTooth
Serial.begin(9600);
Serial1.begin(9600);
pinMode(LEDPIN, OUTPUT);
pinMode(BUZZER, OUTPUT);
}

void loop() {
// Process commands from bluetooth first.
if(Serial1.available() > 0){
String str = Serial1.readString().substring(0);
Serial.println(str);
if(str.indexOf("LED_ON")!=-1){
digitalWrite(LEDPIN, HIGH);
} else if(str.indexOf("LED_OFF")!=-1){
digitalWrite(LEDPIN, LOW);
}
if(str.indexOf("BUZZER_ON")!=-1){
digitalWrite(BUZZER, HIGH);
}else if(str.indexOf("BUZZER_OFF")!=-1){
digitalWrite(BUZZER, LOW);
}
}
}
