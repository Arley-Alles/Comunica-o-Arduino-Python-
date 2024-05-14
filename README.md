<p align="center">
  <img src="/Python_Arduino/data science (1).png" >
</p>

# Comunicao_Arduino/Python

### Neste repositório foi realizada uma comunicação entre dois arduinos (arduino_emissor e arduino_receptor) via WiFi para transmissão de dados de tensão elétrica através de uma das I/O analógicas do microcontrolador. Neste caso o operador de um determinado equipamento pode realizar as aferições de tensão a longas distâncias.
### Equipamentos utilizados:
* **2 arduinos nano ou uno;**
* **2 módulos RF24l01;**
### Códigos:
* **Arduino_emissor:** https://github.com/Arley-Alles/Comunica-o-Arduino-Python-/blob/main/Emissor%20RF24.ino;
* **Arduino_receptor:** https://github.com/Arley-Alles/Comunica-o-Arduino-Python-/blob/main/Receptor%20RF24.ino;

### Posteriormente, foi feita uma comunicação entre o arduino_receptor e o python para fazer a leitura das informações recebidas de forma dinâmica e futuramente, salvar as infromações em uma planilha de excel.

### Código:
* **Leitura arduino_receptor/python:** https://github.com/Arley-Alles/Comunica-o-Arduino-Python-/blob/main/Leitura_dinamica.py;
