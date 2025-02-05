#“FizzBuzz” é um problema clássico de programação. O programa recebe um número inteiro e imprime: a. “Fizz", caso o número seja múltiplo de 3. b. “Buzz", caso o número seja múltiplo de 5. c. “FizzBuzz", caso o número seja múltiplo de 3 e de 5.
num = 1
while num != 0:
  num = int(input("Digite um número: "))
  if num%3 == 0 and num%5 == 0:
    print("FizzBuzz")
  elif num%3 == 0:
    print("Fizz")
  elif num%5 == 0:
    print("Buzz")

#Escreva um programa que receba um número inteiro n e imprima a soma de todos os números de 1 até n (inclusive n ).
n = int(input("Digite um número: "))
i = 0
while i<n:
  i+=1
  print(i)

