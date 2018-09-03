# coding utf-8

import socket as skt
import json as JSON

PORT = 25900
SERVER = '10.3.1.21'


def soma(x, y):
    return communicate_rpc('+', x, y)


def subtracao(x, y):
    return communicate_rpc('-', x, y)


def multiplicacao(x, y):
    return communicate_rpc('*', x, y)


def divisao(x, y):
    return communicate_rpc('/', x, y)


def communicate_rpc(operacao, arg1, arg2):
    tcp = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    tcp.connect((SERVER, PORT))

    send_json = {'op': operacao, 'n1': arg1, 'n2': arg2}

    tcp.send(JSON.dumps(send_json).encode('utf-8'))

    result = tcp.recv(1024).decode('utf-8')

    tcp.close()

    return result
