from tarefas import Tarefas
import os

class Menu():
    def __init__(self):
        self.tarefas = Tarefas()

    #personalizar visualmente no terminal
    def personalizar(self):
        print('-'*40)
    
    #limpar o terminal
    def limpar(self):
        os.system('cls')

    def mostraMenu(self):

         while True:
            self.personalizar()
            titulo = 'Menu'
            print(titulo.center(40))
            print('1-Adicionar Tarefa')
            print('2-Listar Tarefa')
            print('3-Remover Tarefa')
            print('4-Sair')
            self.personalizar()
        
            numero = int(input('Escolha sua opção: '))
            if numero == 1:
                self.limpar()
                self.personalizar()
                self.tarefas.adicionaTarefa()
                self.personalizar()
            elif numero == 2:
                self.limpar()
                self.personalizar()
                self.tarefas.listarTarefa()
                self.personalizar()
                #listarTarefa()
            elif numero == 3:
                self.limpar()
                self.personalizar()
                self.tarefas.removerTarefa()
                self.personalizar
                #removerTarefa()
            elif numero == 4:
                self.limpar()
                self.personalizar()
                self.tarefas.sair()
                self.personalizar()
                break
                #sair()
            else: 
                print('Digite uma opção entre 1 e 4')

   