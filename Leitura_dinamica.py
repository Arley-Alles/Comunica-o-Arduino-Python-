# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:16:32 2021

@author: Arley
"""

"""-------------------------------- Bibliotecas utilizadas -------------------------------------------------"""
import matplotlib.gridspec as gridspec
import serial
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
import win32api
import time
import datetime
import warnings
warnings.filterwarnings("ignore")


"""----------------Identificando a porta em que o arduino está conectado e a baud rate-----------------------"""

arduinoData = serial.Serial('COM5', 9600) #Porta que o arduino está conectado e a baud rate
plt.ion()


"""------------------------Algumas variáveis para o loop e coleta dos dados----------------------------------"""
cont            = 0
tempo           = 0
arm_tempo       = [] #Armazenamento parcial do tempo.  Apenas para o gráfico
tensao          = [] #Armazenamento parcial da tensão. Apenas para o gráfico
arm_tempo_total = [] #Armazenamento total do tempo.  Apenas para o excel
tensao_total    = [] #Armazenamento total da tensão. Apenas para o excel

""""------------------------ Checando o estado do botão de acionamento ---------------------------------------"""
estado_botao = win32api.GetKeyState(0x43) #Neste caso é o botão "C" 

if (estado_botao == 1):
    print("")
    print("######################## AVISO ###########################")
    print("")
    print("Favor pressionar o botão C do computador para inicializar a aquisição de dados")
    arduinoData.close()
    
else:
   
    def grafico():
        plt.ylim(0, 7)
        plt.xlabel("Tempo (segundos)")
        plt.ylabel("Tensão (Volts)")
        plt.plot(arm_tempo, tensao, 'ro--')

    """---------------------------Loop que define quantos dados serão coletados----------------------------------"""

    while (estado_botao == 0):
        
        #Condição para esperar até que hajam dados no arduino para serem 
        #transmitidos para o python
        while(arduinoData.inWaiting() == 0): 
            pass
    
        #Leitura dos dados via serial
        Dados= arduinoData.readline()
        
        #Print e Armazenamento dos dados coletados
        new_Dados= Dados.decode().strip('\r\n')
        print("O valor da tensão é de:", float(new_Dados), "Volts")
        tensao.append(float(new_Dados))
        tensao_total.append(float(Dados))
        
        #Valor acrescentado em cada loop. É o mesmo valor que o comando time.sleep
        tempo += 0.1                       
        arm_tempo.append(tempo)
        arm_tempo_total.append(tempo)
        
        #Print em tempo real
        drawnow(grafico)
        
        #Este contador é para controlar o número de pontos mostrados no gráfico 
        #(Comando if abaixo)
        cont  += 1

        if (cont > 50):
            tensao.pop(0)
            arm_tempo.pop(0)
            
        #Checar o estado do botão "C"
        estado_botao = win32api.GetKeyState(0x43) 
        
        #Comando usado para contar o tempo
        time.sleep(0.1) 
        
    #Etapa de salvamento dos dados em planilha de excel    
    if (estado_botao == 1):
        
        dataset = {"Tempo (segundos)": arm_tempo_total, 
                   "Tensão(volts)": tensao_total} #Transformando em dicionário
        
        ARM_DADOS= pd.DataFrame(dataset)
        #ARM_DADOS.to_csv('/home/arley/Documentos/Doutorado/Dados_Doutorado/Dados_50khz.csv', index= False, header= True)
        print("")
        print("######################## AVISO ###########################")
        print("")
        print("Aquisição de dados finalizada")
        
        salvar = input("Deseja salvar o dataset em uma planilha de excel: ")
        
        if (salvar == "Sim") or (salvar == "sim") or (salvar == "SIM"):
            
            ARM_DADOS.to_excel(r'C:\Users\Arley\OneDrive\Documentos\Python Scripts\Programas doutorado\Dados_cronoamperometria.xlsx', 
                               index= False, header= True)
                    
    
    arduinoData.close()