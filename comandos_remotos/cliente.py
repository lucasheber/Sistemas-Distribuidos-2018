#coding utf-8

import socket as socket


portaServidor = 12002
servidor = '127.0.0.1'

while True:
    print("Digite o comando: ")
    busca = input()

    if busca == 'exit':
        break;

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((servidor, portaServidor))
    tcp.send(busca.encode('utf-8'))

    resposta = tcp.recv(1024).decode()
    print(resposta)

    tcp.close()
