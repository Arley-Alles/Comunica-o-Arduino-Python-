//###############################################################//
//#                                                             #//  
//#                    Arduino_receptor                         #//
//#                                                             #//
//###############################################################//


//Biblioteca responsável pelo funcionamento do módulo RF24l01
#include <RF24.h>

//########################## Variáveis criadas ###########################
RF24 radio(7, 8); //Pinos enable e select do RF24
const byte address[6] = "00001"; //Endereço para estabelecer a comunicação entre os arduinos. Deve ser o mesmo nos dois microcontroladores
float OUT; //Variável do valor lido de tensão de saída


//###################### Inicialização do RF24l01 #######################
void setup() {

Serial.begin(9600);
radio.begin();

radio.openReadingPipe(0, address);
radio.startListening();
 
}


//################# Leitura do sinal do arduino_emissor ##################
void loop() {

if (radio.available()){

  radio.read(&OUT, sizeof(float));
  Serial.println(OUT);
  delay(500);

  }

}
