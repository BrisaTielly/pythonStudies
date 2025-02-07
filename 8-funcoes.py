#1- Função que recebe uma lista e retorna uma tupla com o maior número e sua posição
def tupla(list):
  tup = ()
  value = max(list)
  i = 0
  for num in list:
    if num == value:
      tup = (i, value)
      return tup
    else:
      i+=1
lista = [1, 2, 3, 4, 10, 8, 6]
print(tupla(lista))

#2- mplemente uma função que recebe dois argumentos, uma lista e um elemento , e retorna True caso elemento seja encontrado na lista , e False caso contrário. Não é permitido utilizar o método in .
def exists(list, element):
  i = 0
  while i < len(lista):
        if element == lista[i]:
            return True
        i += 1
  return False

lista = [1, 2, 3, 4, 10, 8, 6]
print(exists(lista, 50))

#3- Fatorial
def fatorial (num):
  i = 1
  sum = 1
  while num>i:
    sum *= i
    i+=1
  print(sum)

fatorial(10)
