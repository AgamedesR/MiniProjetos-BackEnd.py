#

import os

# [] = lista de restaurantes para armazenar os restaurantes cadastrados.
# {} = armazena todas as informações(dicionario) referente ao restaurante.
# Chave-Valor : 'nome' = chave, 'Dona Maria' = valor
restaurantes = [{'nome': 'Dona Maria', 'categoria': 'Comida Caseira', 'ativo':False}, 
                {'nome': 'Pizza DaHORA', 'categoria': 'Pizzaria', 'ativo':True}, 
                {'nome': 'Carne e Brasa', 'categoria': 'Churrascaria', 'ativo':False}
                
]

def exibir_nome_do_programa():
      ''' Exibe o nome estilizado do programa na tela '''
      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
      ''' Exibe as opções disponíveis no menu principal '''
      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurantes')
      print('3. Alterar Status do Restaurante')
      print('4. Sair\n')

def finalizar_app():
     ''' Exibe mensagem de finalização do aplicativo '''
     exibir_subtitulo('Finalizar app')

def voltar_menu_principal():
      ''' Solicita uma tecla para voltar ao menu principal 

    - Outputs: Retorna ao menu principal
    '''
      input('\nDigite uma tecla para voltar ao menu principal: ')
      main()

def opcao_invalida():
      ''' Exibe mensagem de opção inválida e retorna ao menu principal 

    - Outputs: Retorna ao menu principal
    '''
      print('Opção inválida!\n')
      voltar_menu_principal()

def exibir_subtitulo(texto):
      ''' Exibe um subtítulo estilizado na tela 

    - Inputs: texto: str - O texto do subtítulo
    '''
      os.system('cls')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      '''Função para cadastrar um novo restaurante.

      - Inputs: Nome do restaurante, categoria do restaurante.
      - Output: Adiociona um novo restaurante à lista de restaurantes.

      '''
      exibir_subtitulo('Cadastro de Novo Restaurante')
      nome_do_restaurante = input('Digite o nome do restaurante a ser cadastrado: ')
      categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
      # append = método utilizado para adicionar um item a uma lista.
      # (nome_do_restaurante) é o item que queremos adicionar à lista restaurantes.
      restaurantes.append(dados_do_restaurante)
      print(f'\nO restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!\n')

      voltar_menu_principal()

def listar_restaurantes():
      ''' Lista os restaurantes presentes na lista 
    
- Outputs: Exibe a lista de restaurantes na tela
    '''
      exibir_subtitulo('Lista de Restaurantes Cadastrados')

      print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | STATUS')
      # Para cada restaurante na lista de restaurantes, imprima o nome do restaurante.
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome'] 
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            # ljust (Left Justify) = ajusta o texto para a esquerda e preenche o restante com espaços até atingir um tamanho definido.
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_menu_principal()

def alterar_status_do_restaurante():
      '''Altera o estado ativo/desativado de um restaurante
      
      - Output: Mensagem indicando sucesso na operação.
      
      '''
      exibir_subtitulo('Alterar Status do Restaurante')
      nome_restaurante = input('Digite o nome do restaurante para alterar o status: ')
      restaurante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  # O restaurante foi encontrado!
                  restaurante_encontrado = True
                  # O operador 'not' é utilizado para inverter o valor de uma expressão booleana.
                  restaurante['ativo'] = not restaurante['ativo']
                  # Condição Ternária -> É uma forma de escrever uma expressão condicional em uma única linha de código.
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!' 
                  print(mensagem)
      if not restaurante_encontrado: 
            print('O restaurante não foi encontrado.')

      voltar_menu_principal()


def escolher_opcao():
      '''Solicita e executa a opção escolhida pelo usuário
      
      - Input: Opção escolhida pelo usuário.
      
      '''
      try:
            apcao_escolhida = int(input('Digite a opção desejada: '))
            #opcao_escolhida = int(opcao_escolhida)

            if apcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif apcao_escolhida == 2:
                  listar_restaurantes()
            elif apcao_escolhida == 3:
                  alterar_status_do_restaurante()
            elif apcao_escolhida == 4: 
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
     '''Função principal do programa, oone todas as outras funções são chamadas.'''
     os.system('cls')
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()

# Quando pedimos para que um programa Python seja executado, o interpretador cria uma variável chamada __name__. 
# Se o __name__ for __main__, significa que esse código não será importado por outros scripts de código Python, e ele será o programa principal.
if __name__ == '__main__':
      main()