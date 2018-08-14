# coding utf-8

import socket as socket
import subprocess as process

portaServidor = 12002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = ('127.0.0.1', portaServidor)
tcp.bind(origem)
tcp.listen(1)

while True:

    conexao, cliente = tcp.accept()
    comando = conexao.recv(2048).decode()

    if comando.lower() == "exit":
        break

    resposta = process.check_output(comando, universal_newlines=True, shell=True, stderr=process.STDOUT)

    conexao.send(resposta.encode('utf-8'))



print("Servidor desconectado!")
tcp.close()
