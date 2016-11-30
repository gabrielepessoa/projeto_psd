from flask import Flask
app = Flask(__name__)

time_a = {'Dennis_Dotterweich':{'1:1':0,'1:2':0,'1:3':0,'1:4':0,'1:5':0,'1:6':6,'1:7':0,'1:8':0,'1:9':0,'1:10':0,'1:11':0,'1:12':0,'1:13':0,'2:1':0,'2:2':0,'2:3':0,'2:4':0,'2:5':0,'2:6':0,'2:7':0,'2:8':0,'2:9':0,'2:10':0,'2:11':0,'2:12':0,'2:13':0,'3:1':0,'3:2':0,'3:3':0,'3:4':0,'3:5':0,'3:6':0,'3:7':0,'3:8':0,'3:9':0,'3:10':0,'3:11':0,'3:12':0,'3:13':0,'4:1':0,'4:2':0,'4:3':0,'4:4':0,'4:5':0,'4:6':0,'4:7':0,'4:8':0,'4:9':0,'4:10':0,'4:11':0,'4:12':0,'4:13':0,'5:1':0,'5:2':0,'5:3':0,'5:4':0,'5:5':0,'5:6':0,'5:7':0,'5:8':0,'5:9':0,'5:10':0,'5:11':0,'5:12':0,'5:13':0,'6:1':0,
'6:2':0,'6:3':0,'6:4':0,'6:5':0,'6:6':0,'6:7':0,'6:8':0,'6:9':0,'6:10':0,'6:11':0,'6:12':0,'6:13':0,'7:1':0,'7:2':0,'7:3':0,'7:4':0,'7:5':0,'7:6':0,'7:7':0,'7:8':0,'7:9':0,'7:10':0,'7:11':0,'7:12':0,'7:13':0,'8:1':0,'8:2':0,'8:3':0,'8:4':0,'8:5':0,'8:6':0,'8:7':0,'8:8':0,'8:9':0,'8:10':0,'8:11':0,'8:12':0,'8:13':0,'0:0':0}}

#retornando a quantidade de vezes que o jogador apareceu em todas as posicoes
@app.route('/time_a/<jogador>/')
def get_jogador(jogador):
    return str(time_a[jogador])

#retornando quantidade em posicao especifica
@app.route('/time_a/<jogador>/<posicao>/')
def get_posicao(jogador, posicao):
    return str(time_a[jogador][posicao])

#incrementando posicao
@app.route('/add/time_a/<jogador>/<posicao>/')
def add_posicao(jogador, posicao):
    try:
        time_a[jogador][posicao]+=1
        print ("Adicionado")
    except:
        print ('except')
        time_a[jogador]['0:0']+=1

    return ('Posicao Adicionada')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
