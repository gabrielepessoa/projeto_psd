from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.mqtt import MQTTUtils
import requests


sc = SparkContext()
ssc = StreamingContext(sc, 1)


def posicao_matriz(valores_fila):
        pos = valores_fila.split(".")
        x,y = int(pos[0]),int(pos[1])
        px = int(x/5225)
        py = int((33965 -y)/(6560.375))
        pos_matriz = (str(px)+":"+str(py))
        #print("x : "+str(x) + " y : " + str(y))
        response = requests.get("http://192.168.25.25:5000/add/time_a/Dennis_Dotterweich/" + pos_matriz) #ipdeondeestarodandoowebservice
        print ("http://192.168.25.25:5000/add/time_a/Dennis_Dotterweich/"+ pos_matriz)
        print response.content

        return ("Posicao da matriz: " + pos_matriz)


mqttStream = MQTTUtils.createStream(#DStream
    ssc,
    "tcp://localhost:1883",  # Note both port number and protocol
    "Dennis Dotterweich perna direita"                  # The same routing key as used by producer
)
#mqttStream.count().pprint()
mqttStream.map(posicao_matriz).pprint()

ssc.start()
ssc.awaitTermination()
ssc.stop()

print max(Dennis_Dotterweich, key=Dennis_Dotterweich.get)
print ("fora ="+str(Dennis_Dotterweich['0:0']))
