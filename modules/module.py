# coding utf-8

import socket as skt
import json as JSON

PORT = 25000
SERVER = '10.3.1.21'


def soma(x, y):
    return communicate_rpc('sum', x, y)


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


def communicate_rpc(operacao, arg1, arg2):
    skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    skt.connect((SERVER, PORT))

    send_json = "{" + 'op: "{}", n1: {}, n2: {}'.format(operacao, arg1, arg2) + "}"

    skt.send(JSON.dumps(send_json))

    print(skt.recv(1024))

    skt.close()

