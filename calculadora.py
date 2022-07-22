n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    opcao = float(input('Qual operação deseja realizar?: '
                      '[1]Somar'
                      '[2]Subtrair'
                      '[3]Dividir'
                      '[4]Multiplicar'
                      '[5]Sair do programa: '))
    if opcao == 1:
        print('A soma de {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A subtração de {} e {} é igual a {}'.format(n1, n2, n1 - n2))
    elif opcao == 3:
        print('A divisão de {} e {} é igual a {}'.format(n1, n2, n1 / n2))
    elif opcao == 4:
        print('A multiplicação de {} e {} é igual a {}'.format(n1, n2, n1 * n2))
print('Até a próxima')