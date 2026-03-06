import os

def exibir_nome_do_programa():
    print("""
           ********************************
            CALCULADORA MATEMÁTICA SIMPLES
           ********************************
""")
        
def exibir_opcoes():
    print('Escolha a operação desejada:')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Finalizar Calculadora\n')

def escolher_opcoes():
    opcao_escolhida = int(input('Digite o número da opção desejada: '))
    try:
        if opcao_escolhida == 1:
            operacao_somar()
        elif opcao_escolhida == 2:
            operacao_subtrair()
        elif opcao_escolhida == 3:
            operacao_multiplicar()
        elif opcao_escolhida == 4:
            operacao_dividir()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('\nOpção inválida!')
    voltar_menu_principal()
    
def voltar_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal: ')
      main()

def finalizar_app():
    exibir_subtitulo('Operação da Calculadora Finalizada!')

def solicitar_numeros():
    primeiro_numero = int(input('Digite o primeiro número inteiro: '))
    segundo_numero = int(input('Digite o segundo número inteiro: '))
    return primeiro_numero, segundo_numero

def operacao_somar():
    exibir_subtitulo('Operação de Soma')
    primeiro_numero, segundo_numero = solicitar_numeros()
    soma = primeiro_numero + segundo_numero
    print(f'A soma dos números é: {soma}')
    voltar_menu_principal()

def operacao_subtrair():
    exibir_subtitulo('Operação de Subtração')
    primeiro_numero, segundo_numero = solicitar_numeros()
    subtracao = primeiro_numero - segundo_numero
    print(f'A subtração dos números é: {subtracao}')
    voltar_menu_principal()

def operacao_multiplicar():
    exibir_subtitulo('Operação de Multiplicação')
    primeiro_numero, segundo_numero = solicitar_numeros()
    multiplicacao = primeiro_numero * segundo_numero
    print(f'A multiplicação dos números é: {multiplicacao}')
    voltar_menu_principal()

def operacao_dividir():
    exibir_subtitulo('Operação de Divisão')
    primeiro_numero, segundo_numero = solicitar_numeros()
    divisao = primeiro_numero / segundo_numero
    print(f'A divisão dos números é: {divisao}')
    voltar_menu_principal()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()
