#1- Escreva um programa que lê números inteiros positivos do usuário, um após o outro, e monta uma lista a partir desses números e depois imprime a lista montada. O programa deve continuar solicitando por números até que o elemento digitado seja um número negativo (que não deve ser inserido na lista).

list = []
while True:
  x = int(input("Insira um número: "))
  if x<0:
    break
  list.append(x)

print(list)

#2- Dada uma lista de números inteiros, escreva um programa que calcula a soma de todos os números na lista.
list = [1, 10, 20, 35, 22, 12]
x=0
for num in list:
  x+=num
print(x)

#3- Data uma lista de números inteiros, escreva um programa que calcula a média dos números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3 deve imprimir apenas 12 .
list = [1, 10, 20, 35, 22, 12]
sum=0
for num in list:
  sum+=num
print(sum//len(list))

#3- Alunos e suas respectivas notas, Escreva uma programa que calcula a média das notas de todos os alunos.
students = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]
sum = 0
for num in students:
  sum+= num[1]
print(sum//len(students))

# Alunos e suas notas representados através de dicionários
students = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]

sum = 0
for grade in students:
  sum+= grade["nota"]
print(sum//len(students))

#4- DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime o maior número dessa lista.
lista = [1, 3, 2, 5]
print(max(lista))

#5- Escreva um programa que solicite uma string para o usuário e imprima quantas vezes cada letra aparece na palavra. Por exemplo:
map = {}
word = input("Insira uma palavra: ")
for l in word:
  if l in map:
    map[l] += 1
  else:
    map[l] = 1

print(map)  