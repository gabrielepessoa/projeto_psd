from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.mqtt import MQTTUtils

sc = SparkContext()
ssc = StreamingContext(sc, 1)

Dennis_Dotterweich = {'1:1':0,'1:2':0,'1:3':0,'1:4':0,'1:5':0,'1:6':0,'1:7':0,'1:8':0,'1:9':0,'1:10':0,'1:11':0,'1:12':0,'1:13':0,'2:1':0,'2:2':0,'2:3':0,'2:4':0,'2:5'$
'6:2':0,'6:3':0,'6:4':0,'6:5':0,'6:6':0,'6:7':0,'6:8':0,'6:9':0,'6:10':0,'6:11':0,'6:12':0,'6:13':0,'7:1':0,'7:2':0,'7:3':0,'7:4':0,'7:5':0,'7:6':0,'7:7':0,'7:8':0,'7:$

def posicao_matriz(valores_fila):
        pos = valores_fila.split(".")
        x,y = int(pos[0]),int(pos[1])
        px = int(x/5225)
        py = int((33965 -y)/(6560.375))
        pos_matriz = (str(px)+":"+str(py))
        print("x : "+str(x) + " y : " + str(y))
        try:
                Dennis_Dotterweich[pos_matriz] = Dennis_Dotterweich[pos_matriz] + 1
        except:
                print("except")
                Dennis_Dotterweich['0:0'] = Dennis_Dotterweich['0:0'] + 1

        return ("Posicao da matriz: " + pos_matriz)
mqttStream = MQTTUtils.createStream(#DStream
    ssc,
    "tcp://localhost:1883",  # Note both port number and protocol
    "Dennis Dotterweich perna direita"                  # The same routing key as used by producer
)
#mqttStream.count().pprint()
mqttStream.map(posicao_matriz).pprint()

ssc.start()
ssc.awaitTermination(10)
ssc.stop()

print max(Dennis_Dotterweich, key=Dennis_Dotterweich.ge