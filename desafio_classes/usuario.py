class Usuario:
  quantidade = 0
  def __init__(self, nome, email):
    self.nome = nome
    self.email = email
    Usuario.quantidade+=1

  
  def imprime_usuario(self):#Com certeza tem um jeito melhor de printar isso...
    print(self.nome + "(" + self.email + ")")
