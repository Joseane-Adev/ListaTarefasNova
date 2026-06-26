class Tarefas():
    def __init__(self):
      self.lista = []
    
    def adicionaTarefa(self):
        tarefa = input('Digite a tarefa: ').capitalize()
        print(f'Tarefa {tarefa} registrada!')
        self.lista.append(tarefa)
        #chamar menu()
        #chamar opcao()
    
    def listarTarefa(self):
       #mostrar lista
       
       titulo = 'Lista de tarefas:'
       print(titulo.center(40))
       for indice,nometarefa in enumerate(self.lista, start=1):
          print(f'[{indice}] {nometarefa}')
       
    
    def removerTarefa(self):
       #mostrar a lista e depois escolher qual quer apagar
       self.listarTarefa()
       escolha = int(input('Escolha o numero da tarefa para remover: '))
       try:
            tarefa_removida = self.lista[escolha - 1]
            '''
            o indice começa por 0, coloquei a lista para começar por 1.
            entao é feito a conta o valor que você escolheu - 1 ai dá a posição do indice
            '''
            del self.lista[escolha - 1]
            print(f'Removido da lista: {tarefa_removida}')
       except (ValueError, IndexError):
           print('Valor não encontrado, verifique a lista')
    
    def sair(self):
        print('Você saiu do programa')
        


       