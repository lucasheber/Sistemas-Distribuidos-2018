# coding utf-8

import module as m


def main():
    x = 5
    y = 0

    print("Soma de {} + {} = {}".format(x, y, m.soma(x, y)))
    print("Subt de {} - {} = {}".format(x, y, m.subtracao(x, y)))
    print("Divi de {} / {} = {}".format(x, y, m.divisao(x, y)))
    print("Mult de {} * {} = {}".format(x, y, m.multiplicacao(x, y)))


if __name__ == '__main__':
    main()
