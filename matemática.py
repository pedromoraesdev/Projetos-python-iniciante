from math import sqrt
from time import sleep
name = str(input('Digite seu nome: '))
print('Seja bem vindo ao mundo de inteligência artificial do python {}.\n'
      'Aqui você vai poder calcular Bhaskara, área e perímetro de um círculo, raizes diversas\n'
      ''.format(name))
choice = int(input('Digite o valor correspondente a sua vontade\n'
                   '[1]Bhaskara\n'
                   '[2]Área e perímetro de um círculo\n'
                   '[3]Raizes\n'
                   '[4] Sair do programa:\n'))
while not choice == 4:
    if choice == 1:
        print(
            'Olá {}, eu sou uma calculadora de Bhaskara, e meu objetivo é mostrar como o pensamento computacional é incrível e rápido.'.format(name))
        print('Coloque os valores de cada coeficiente.')
        a = float(input('Digite o valor do coeficiente a: '))
        b = float(input('Digite o valor do coeficiente b: '))
        c = float(input('Digite o valor do coeficiente c: '))
        delta = b ** 2 - 4 * a * c
        print('Calculando delta...')
        sleep(2)
        print('O valor de delta é {:.2f}'.format(delta))
        raiz = delta ** 0.5
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        print('Calculando x1 e x2...')
        sleep(2)
        print('O valor de x1 é {:.2f}'.format(x1))
        print('O valor de x2 é {:.2f}'.format(x2))
        sleep(3)
        print('Seja bem vindo ao mundo de inteligência artificial do python {}.\n'
              'Aqui você vai poder calcular Bhaskara, área e perímetro de um círculo, raizes diversas\n'
              ''.format(name))
        choice = int(input('Digite o valor correspondente a sua vontade\n'
                           '[1]Bhaskara\n'
                           '[2]Área e perímetro de um círculo\n'
                           '[3]Raizes\n'
                           '[4] Sair do programa:\n'))
    elif choice == 2:
            print('Bem vindo {}, vamos calcular o perímetro e área de um círculo'.format(name))
            print('Então por favor, informe o valor do raio')
            pi = 3.14
            print('Antes do cálculo, vamos relembrar que o perímetro se calcula por: 2.𝝿.R')
            print('E a área se calcula por: 𝝿.R²')
            r = float(input('Digite o valor do raio (pode ser um número decimal): '))
            per = 2 * pi * r
            ar = pi * r ** 2
            print('Calculando o perímetro...')
            sleep(1.5)
            print('Agora, calculando a área...')
            sleep(1)
            print('Os valores da área e do perímetro respectivamente são {:.2f} e {:.2f}'.format(per, ar))
            sleep(3)
            print('Seja bem vindo ao mundo de inteligência artificial do python.\n'
                  'Aqui você vai poder calcular Bhaskara, área e perímetro de um círculo, raizes diversas\n'
                  '')
            choice = int(input('Digite o valor correspondente a sua vontade\n'
                               '[1]Bhaskara\n'
                               '[2]Área e perímetro de um círculo\n'
                               '[3]Raizes\n'
                               '[4] Sair do programa:\n'))
    elif choice == 3:
                print('Ola, eu irei calcular qualquer raiz que você pedir de quaquer número, faça o teste')
                print('Antes vamos lembrar, temos o índice de uma raiz (número que está fora da raiz);\n'
                      'Temos o radicando (número dentro da raiz)\n'
                      'E por último, podemos ter o radicando elevado a algum número (caso não tenha é 1)')
                x = float(input('Digite o valor do radicando:  '))
                m = float(input('Digite o expoente do radicando ( caso não tenha, digite 1): '))
                n = float(input('Digite o índice da raiz: '))
                raiz = x ** (m / n)
                print('Calculando o valor da raiz...')
                sleep(2.5)
                print('O valor é {:.2f}'.format(raiz))
                sleep(3)
                choice = int(input('Digite o valor correspondente a sua vontade\n'
                                   '[1]Bhaskara\n'
                                   '[2]Área e perímetro de um círculo\n'
                                   '[3]Raizes\n'
                                   '[4] Sair do programa:\n'))

print('Até a próxima')






