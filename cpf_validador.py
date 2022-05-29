def entrada_int(msg):
    """
    FUNÇÃO PARA TRATAR ENTRADA DE DADOS DO TIPO INTEIRO
    :param msg: RECEBER A MENSAGEM DE INPUT
    :return: RETORNA O VALOR DE N OU ALGUM ERRO!
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário!")
        else:
            return n

while True:
    cpf = str(entrada_int('Digite um CPF ou [0] para sair: ')) # ENTRADA DE DADOS COM A FUNÇÃO
    if cpf == '0':
        break
    cpf1 = cpf[:9]                   # ELIMINA OS DOIS ÚLTIMOS NÚMEROS DO CPF

    reverso = 10                      # CONTADOR REVERSO
    total = 0
    for i in range(19):
        if i > 8:                           # PRIMEIRO ÍNDICE VAI DE 0 A 9
            i -= 9                          # OS 9 PRIMEIROS DIGITOS DO CPF
        total += int(cpf1[i]) * reverso     # TOTAL ACUMULA O TOTAL DA MULTIPLICAÇÃO

        reverso -= 1                        # DECREMENTO DO CONTADOR REVERSO
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0                      # ZERANDO O TOTAL
            cpf1 += str(d)                 # CONCATENANDO O DIGITO GERADO COM O CPF NOVO

    sequencia = cpf1 == str(cpf1[0]) * len(cpf) # exita sequencias 111111111111, 22222222 ....

    if cpf == cpf1 and not sequencia:
        print(f'CPF {cpf} VÁLIDO!')
    else:
        print(f'CPF {cpf} INVÁLIDO!!!')