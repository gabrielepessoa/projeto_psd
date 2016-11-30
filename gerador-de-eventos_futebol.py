# -*- coding: cp1252 -*-

import time
import pika
global connection
global channel
global TIME_INTERVAL
global START_OF_MATCH
global END_OF_MATCH
from datetime import datetime      


''' def criarFilas():
       #id bola = 4,8,10,12
        channel.queue_declare(queue='Bola')
        channel.queue_declare(queue='topic')

        #Fila para enviar os eventos que não se enquadram em nenhuma das fila abaixo 
        channel.queue_declare(queue='Outros') 

        #Time A
        channel.queue_declare(queue='Nick Gertj perna direita')
        channel.queue_declare(queue='Nick Gertj perna esquerda')
        channel.queue_declare(queue='Nick Gertj mao direita')
        channel.queue_declare(queue='Nick Gertj mao esquerda')

        channel.queue_declare(queue='Dennis Dotterweich perna direita') 

        channel.queue_declare(queue='Dennis Dotterweich perna esquerda')
        channel.queue_declare(queue='Niklas Waelzlein perna direita')
        channel.queue_declare(queue='Niklas Waelzlein perna esquerda')
        channel.queue_declare(queue='Wili Sommer perna esquerda')
        channel.queue_declare(queue='Wili Sommer perna direita')
        channel.queue_declare(queue='Roman Hartleb perna direita')
        channel.queue_declare(queue='Roman Hartleb perna esquerda')
        channel.queue_declare(queue='Erik Engelhardt perna direita')
        channel.queue_declare(queue='Erik Engelhardt perna esquerda')
        channel.queue_declare(queue='Sandro Schneider perna direita')
        channel.queue_declare(queue='Sandro Schneider perna esquerda')

        #Time B
        channel.queue_declare(queue='Leon Krapf mao direita ')
        channel.queue_declare(queue='Leon Krapf mao esquerda ')
        channel.queue_declare(queue='Leon Krapf perna direita') 
        channel.queue_declare(queue='Leon Krapf perna esquerda')
        channel.queue_declare(queue='Kevin Baer perna esquerda')
        channel.queue_declare(queue='Kevin Baer perna direita')
        channel.queue_declare(queue='Luca Ziegler perna esquerda')
        channel.queue_declare(queue='Luca Ziegler perna direita')
        channel.queue_declare(queue='Ben Mueller perna direita')
        channel.queue_declare(queue='Ben Mueller perna esquerda')
        channel.queue_declare(queue='Vale Reitstetter perna direita')
        channel.queue_declare(queue='Vale Reitstetter perna esquerda')
        channel.queue_declare(queue='Christopher Lee perna direita')
        channel.queue_declare(queue='Christopher Lee perna esquerda')
        channel.queue_declare(queue='Leon Heinze perna direita')
        channel.queue_declare(queue='Leon Heinze perna esquerda')
        channel.queue_declare(queue='Leo Langhans perna direita')
        channel.queue_declare(queue='Leo Langhans perna esquerda') 
'''
		
def enviarPraFila(fila, linhaEvento):				
        channel.basic_publish(exchange = 'amq.topic', routing_key = fila, body = linhaEvento)
        print ("enviou para fila " + linhaEvento)
        
        
def verificarEnviaFila(idSensor,info):

        
        if idSensor == 16:
               #enviarPraFila('Dennis Dotterweich perna direita', info)
               print (info)
               enviarPraFila('Dennis Dotterweich perna direita', (str(info[2])+"."+str(info[3])))
                

'''
        if idSensor == 4 or idSensor == 8 or idSensor == 10 or idSensor == 12:
                enviarPraFila('Bola', info)
        elif idSensor == 13:
                enviarPraFila('Nick Gertj perna esquerda', info)
        elif idSensor == 14:
                enviarPraFila('Nick Gertj perna direita', info)
        elif idSensor == 98:
                enviarPraFila('Nick Gertj mao direita', info)
        elif idSensor == 97:
                enviarPraFila('Nick Gertj mao esquerda', info)
        elif idSensor == 16:
                enviarPraFila('Dennis Dotterweich perna direita', info) 
        elif idSensor == 47:
                enviarPraFila('Dennis Dotterweich perna esquerda', info)
        elif idSensor == 49 :
                enviarPraFila('Niklas Waelzlein perna direita', info)
        elif idSensor == 88:
                enviarPraFila('Niklas Waelzlein perna esquerda', info)
        elif idSensor == 19:
                enviarPraFila('Wili Sommer perna esquerda',info)
        elif idSensor == 52:
                enviarPraFila('Wili Sommer perna direita', info)
        elif idSensor == 24:
                enviarPraFila('Roman Hartleb perna direita', info)
        elif idSensor == 23:
                enviarPraFila('Roman Hartleb perna esquerda', info)
        elif idSensor == 58:
                enviarPraFila('Erik Engelhardt perna direita', info)
        elif idSensor == 57:
                enviarPraFila('Erik Engelhardt perna esquerda', info)
        elif idSensor == 28:
                enviarPraFila('Sandro Schneider perna direita', info)
        elif idSensor == 59:
                enviarPraFila('Sandro Schneider perna esquerda', info)

        #TIME B
        elif idSensor == 100:
                enviarPraFila('Leon Krapf mao direita', info)
        elif idSensor == 99:
                enviarPraFila('Leon Krapf mao esquerda', info)
        elif idSensor == 62:
                enviarPraFila('Leon Krapf perna direita', info) 
        elif idSensor == 61:
                enviarPraFila('Leon Krapf perna esquerda', info)
        elif idSensor == 63:
                enviarPraFila('Kevin Baer perna esquerda', info)
        elif idSensor == 64:
                enviarPraFila('Kevin Baer perna direita', info)
        elif idSensor == 65:
                enviarPraFila('Luca Ziegler perna esquerda', info)
        elif idSensor == 66:
                enviarPraFila('Luca Ziegler perna direita', info)
        elif idSensor == 68:
                enviarPraFila('Ben Mueller perna direita', info)
        elif idSensor == 67:
                enviarPraFila('Ben Mueller perna esquerda', info)
        elif idSensor == 38:
                enviarPraFila('Vale Reitstetter perna direita', info)
        elif idSensor == 69:
                enviarPraFila('Vale Reitstetter perna esquerda', info)
        elif idSensor == 40:
                enviarPraFila('Christopher Lee perna direita', info)
        elif idSensor == 71:
                enviarPraFila('Christopher Lee perna esquerda', info)
        elif idSensor == 74:
                enviarPraFila('Leon Heinze perna direita', info)
        elif idSensor == 73:
                enviarPraFila('Leon Heinze perna esquerda', info)
        elif idSensor == 44:
                enviarPraFila('Leo Langhans perna direita', info)
        elif idSensor == 75:
                enviarPraFila('Leo Langhans perna esquerda', info) 
        else:
                enviarPraFila('Outros', info) '''

def lerArquivo(texto):
        now = datetime.now()
        print ("Começo do bloco")
        bloco = []
        first = texto.readline()
        firstValor = first.split(",")
        timestamp = firstValor[1]
        #so ira começar a enviar para fila a partir de determinado timestamp.
        TIME_INTERVAL = 6000000000000
        START_OF_MATCH = 10753295594424116
        END_OF_MATCH = 14879639146403495
        #END_OF_MATCH = 10758380918029578
        while (int(timestamp) < START_OF_MATCH):
                first = texto.readline()
                firstValor = first.split(",")
                timestamp = firstValor[1]
                idSensor = int(firstValor[0])
        ini = time.time()       
        
        while (int(timestamp) < int(END_OF_MATCH)):
               
                inicio = time.time() 
                bloco.append(timestamp)
                limite = int(timestamp) + TIME_INTERVAL
                while (int(timestamp) < int(limite)):
                        linha = texto.readline()
                        valores = linha.split(",")
                        timestamp = valores[1]
                        idSensor = int(valores[0])
                        bloco.append(timestamp)
                        verificarEnviaFila(idSensor, valores)
                fim = time.time()
                
       
       
               
                
if __name__ == '__main__':
        texto = open("full-game","r")
        #credential = pika.PlainCredentials('guest','guest')
        #connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.25.64',5672,'pratica_um',credential))
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.25.32'))
        channel = connection.channel()
        channel.exchange_declare(exchange='amq.topic', type='topic', durable=True)
        print ("conectou")
        #criarFilas()
        lerArquivo(texto)
        print("enviou\o/\o/\o/\o/")
        texto.close()


