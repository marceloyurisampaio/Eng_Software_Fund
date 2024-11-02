##Criação de classes##
class carro:
  #Função que instancia o objeto
  def __init__(self,marca,modelo,cor):
    carro.marca = marca
    carro.modelo = modelo
    carro.cor = cor
  
  #Método de aceleração do carro. 
  def acelerar (self, percent):
    print ("Voce acelerou " + str(percent) + "% no carro")
  
  #Método de freio do carro. 
  def freiar (self, percent):
    print ("Voce freiou " + str(percent) + "% no carro")
  
carro1 = carro("volkswagen", "polo", "azul")
carro1.acelerar(50)

##Definindo privaciade dos métodos e atributos##

class conta_bancaria: 
  def __init__(self, titular, saldo):
    self.titular = titular
    self.__saldo = saldo #Aqui com __ estou definindo que esse atributo é privado, ou seja, nao consigo acessar diretamente fazendo conta.saldo

  #Definindo os métodos
  #Acessar a quantidade de saldo
  def get_saldo(self):
    return self.__saldo
  
  #Setter para modificar o saldo
  def set_saldo (self, valor):
    if valor >= 0:
      self.__saldo = valor
    else:
      print("Saldo não pode ser negativo.")
  
  #Método protegido
  def _mostrar_informacoes (self):
    print("Titular: {self.titular}, Saldo: {self.__saldo}")

# Uso da classe
conta = conta_bancaria("João", 1000)
print(conta.get_saldo())  # Saída: 1000
conta.set_saldo(500)      # Atualiza o saldo
print(conta.get_saldo())   # Saída: 500
conta.set_saldo(-100)      # Tentativa inválida, sem alteração

##Usando o conceito de herança para criar classes derivadas##
# Classe Pai
class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def emitir_som(self):
        print("O animal faz um som.")

# Classe Filha (herda de Animal)
class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro late.")

    def correr(self):
        print("O cachorro está correndo.")

# Classe Filha (herda de Animal)
class Gato(Animal):
    def emitir_som(self):
        print("O gato mia.")

# Criando instâncias
animal = Animal("Animal", "geral")
animal.emitir_som()    # Saída: O animal faz um som.

cachorro = Cachorro("Rex","bulldog")
cachorro.emitir_som()   # Saída: O cachorro late.
cachorro.correr()       # Saída: O cachorro está correndo.
print(cachorro.raca)
gato = Gato("Mimi", "Siames")
gato.emitir_som()       # Saída: O gato mia.
print(gato.raca)

##Polimorfismo##
class Animal:
    def emitir_som(self):
        pass  # Método genérico, que será implementado nas subclasses

class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro late."

class Gato(Animal):
    def emitir_som(self):
        return "O gato mia."

class Vaca(Animal):
    def emitir_som(self):
        return "A vaca muge."

# Função que aceita qualquer tipo de animal e chama o método emitir_som
def fazer_som(animal):
    print(animal.emitir_som())

# Criando instâncias de cada classe
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

# Chamando o método fazer_som com diferentes objetos
fazer_som(cachorro)  # Saída: O cachorro late.
fazer_som(gato)      # Saída: O gato mia.
fazer_som(vaca)      # Saída: A vaca muge.


##Criação de um modelo de Banco digital##
class cliente: 
  def __init__(self, nome, cpf, email):
    self.nome = nome
    self.cpf = cpf
    self.email = email
    self.contas = [] #Lista para armazenar as contas associadas ao cliente. Um unico cliente pode ter varias contas. 
  
  def adicionar_conta(self,conta):
    self.contas.append(conta)
  
  def __str__(self):
     return f"CLiente:{self.nome} - CPF: {self.cpf} - Email: {self.email}"

class conta: 
  def __init__(self, numero, cliente):
    self.numero = numero
    self.cliente = cliente
    self.saldo = 0.0
    self.transacoes = [] #Historico de transações

  def depositar (self,valor):
    if valor > 0: 
      self.saldo += valor
      self.transacoes.append(transacao('Deposito',valor))
    else: 
      print("Valor de depósito inválido.")
  
  def sacar(self,valor): 
    if 0 < valor < self.saldo:
      self.saldo -= valor
      self.transacoes.append(transacao('Saque', valor))
    else:
      print("Saldo insuficiente ou valor inválido.")
  
  def exibir_saldo(self):
    print(f"Saldo atual: R$ {self.saldo: .2f}")

  def exibir_histórico (self): 
    for transacao in self.transacoes: 
       print(transacao)
  
  def __str__(self):
    return f"Conta número: {self.numero} - Saldo: R$ {self.saldo: .2f}"

from datetime import datetime

class transacao: 
  def __init__(self, tipo, valor):
    self.tipo = tipo
    self.valor = valor
    self.data = datetime.now()
  
  def __str__(self):
    return f"{self.data.strftime('%Y-%m-%d %H:%M:%S')} - {self.tipo}: R$ {self.valor:.2f}"


#Criando um cleinte
cliente1 = cliente('Marcelo', '073.074.633-00', 'marceloyurisampaio@gmail.com')

#Criando uma conta para o cliente
conta1 = conta('1001', cliente1)

#Associando a conta ao cliente
cliente1.adicionar_conta(conta1)

#Realizando operações na conta
conta1.depositar(1000000)
conta1.sacar(5)
conta1.exibir_saldo()
conta1.depositar(1000000000)
conta1.exibir_histórico()
