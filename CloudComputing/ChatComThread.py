import socket #estabelece comunicações
import threading #realiza gestão de threads
import sys #usuario no cmd escreve e consegue se conectar?

class Servidor:
    #atributo que representa conexão socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #lista que guarda conexões abertas
    conexoes = []
    

    def __init__(self):
        #aqui nosso construtor ouve todas as interfaces de rede pela porta 8000
        self.sock.bind(('0.0.0.0', 8080))
        self.sock.listen(1)


    def handler(self, conexao, endereco):
        while True:
        #quando alguem enviar mensagem ao servidor, guuardamos na variavel dados
            dados = conexao.recv(1024)
            for conectado in self.conexoes:
                conectado.send(dados)
            if not dados:
                print("{}:{} se desconectou".format(endereco[0], endereco[1]))
                self.conexoes.remove(conexao)
                conexao.close()
                break


    def run(self):
    #codigo roda pra sempre
        while True:
            #para cada conexao, guardar ip e porta
            conexao, endereco = self.sock.accept()
            #criar nova thread que tem como alvo o metodo handler, que criamos acima, passando a conexao e o endereco
            threadConexao = threading.Thread(target=self.handler, args=(conexao, endereco))
            threadConexao.daemon = True
            #a thread será executada
            threadConexao.start()
            self.conexoes.append(conexao)
            print("{}:{} se conectou".format(endereco[0], endereco[1]))


class Cliente:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def __init__(self, enderecoServidor):
        #quando o cliente for inicializado, vamos estabelecer uma conexao com servidor
        self.sock.connect((enderecoServidor, 8080))
        
        #depois disso, vamos criar uma thread para permitir que o usuario mande msgs
        threadInput = threading.Thread(target=self.sendMsg)
        threadInput.daemon = True
        threadInput.start()
        
        #enqanto a thread está rodando, vamos ficar exibindo??
        while True:
            dados = self.sock.recv(1024)
            print("{}".format(dados))

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), "utf-8"))

    

#abaixo estamos checando se quando o scripts começou a rodar, se foi passado argumento no cmd
if (len(sys.argv)>1):
    client = Cliente(sys.argv[1])
else:
    server = Servidor()
    server.run()