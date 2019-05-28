CAPACIDADE_INICIAL = 10

class Node:
    def __init__(self, key, nome,idade):
        self.key = key
        self.nome = nome
        self.idade = idade
        self.next = None
    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.nome, self.idade, self.next != None)
    def __repr__(self):
        return str(self)

class HashTable:

    def __init__(self):
        self.capacity = CAPACIDADE_INICIAL
        self.size = 0
        self.buckets = [None]*self.capacity

    def hash(self, key):
        valorhash = key % self.capacity

        return valorhash

    def insert(self, key, nome, idade):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, nome, idade)

            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, nome, idade)
        finish = input('aperte enter para continuar ...')

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:

            return None
        else:
            print('Matricula -> ',node.key)
            print('Nome -> ',node.nome)
            print('Idade -> ',node.idade)
            finish = input('aperte enter para continuar ...')

    def duplicated(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:

            return False
        else:
            return True

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:

            return None
        else:
            self.size -= 1
            result = node.nome
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next

            return 'removido ->' + result

    def show(self):
        for x in range(len(self.buckets)):
            node = self.buckets[x]
            lista = []
            while node is not None :
                prev = node
                if node is not None:
                    lista.append([node.key,node.nome,node.idade])
                else:
                    lista.append(None)
                node = node.next
            print('%d pos = ' % (x),end='')
            print(lista)
        finish = input('aperte enter para continuar ...')

def Menu(HashTab):
    print('PROJETO ESTRUTURA 2 - HASHTABLE ENCADEADO\nMenu:')
    print('1- Inserir Aluno')
    print('2- Buscar Aluno')
    print('3- Remover Aluno')
    print('4- Mostrar Lista')
    print('5- Encerrar\n')
    escolhaMenu = input('opcao -> ')
    if escolhaMenu == '1':
        key = input('Matricula -> ')
        if HashTab.duplicated(int(key)):
            input('Aluno já cadastrado, aperte enter para voltar ...')
            print()
            Menu(HashTab)
        nome = input('nome -> ')
        idade = input('idade -> ')
        HashTab.insert(int(key),nome,idade)
        print()
        Menu(HashTab)

    if escolhaMenu == '2':
        matricula = input('Matricula -> ')
        HashTab.find(int(matricula))
        print()
        Menu(HashTab)

    if escolhaMenu == '3':
        matricula = input('Matricula -> ')
        HashTab.remove(int(matricula))
        finish = input('aperte enter para continuar ...')
        print()
        Menu(HashTab)

    if escolhaMenu == '4':
        HashTab.show()
        print()
        Menu(HashTab)

    if escolhaMenu == '5':
        print('Desligando...')


Table = HashTable()
Menu(Table)
