#coding utf-8


import socket as socket
import commands

portaServidor = 12002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = ( '127.0.0.1', portaServidor )
tcp.bind(origem)
tcp.listen(1)

while True:

    conexao, cliente = tcp.accept()
    comando = conexao.recv(1024).decode()

    resposta = commands.getoutput(comando)
    # print(resposta)

    tcp.send(resposta)

tcp.close()
