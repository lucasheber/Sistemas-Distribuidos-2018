# coding utf-8

import socket as socket
import subprocess as process

portaServidor = 12002
servidor = '127.0.0.1'

while True:
    print("Digite o comando: ")
    comando = input()

    try:

        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect((servidor, portaServidor))
        tcp.send(comando.encode('utf-8'))

        resposta = tcp.recv(2048).decode()
        print(resposta)

        tcp.close()
    except ConnectionRefusedError:
        resposta = process.check_output(comando, universal_newlines=True, shell=True, stderr=process.STDOUT)
        print(resposta)

    if comando == 'exit':
        break

print("Cliente deconectado!")