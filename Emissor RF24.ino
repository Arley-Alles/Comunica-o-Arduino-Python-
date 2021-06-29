//###############################################################//
//#                                                             #//  
//#                    Arduino_emissor                          #//
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

  radio.begin();
  pinMode(A2, INPUT);
  radio.openWritingPipe(address);
  radio.stopListening();

}


//################# Leitura do sinal do arduino_emissor ##################
void loop() {

  OUT = 5.0*analogRead(A2)/1024.0; //Conversão do sinal de 0-1023 para 0-5V
  radio.write(&OUT, sizeof(float));

}
