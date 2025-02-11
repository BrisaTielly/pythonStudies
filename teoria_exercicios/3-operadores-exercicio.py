#1 - Escreva um programa que receba um número inteiro do usuário e imprima True caso o número seja par e False, caso o número seja ímpar.
num = input("Digite um valor: ")
num = int(num)
print(num % 2 == 0)

#2 - Caso o valor da compra somado ao frete seja superior a R$ 100, ou o cliente seja cadastrado no programa de fidelidade, o cupom de desconto pode ser utilizado. Caso contrário, o cupom não pode ser utilizado

valorCompra = float(input("Insira o valor da compra: "))
frete = float(input("Insira o valor do frete: "))
clienteStatus = input("O cliente está cadastrado no programa de fidelidade? s/n ")

booleano2 = (valorCompra + frete < 100) or clienteStatus == "s" 

print("O cupom pode ser utilizado" * booleano2 or "O cupom não pode ser utilizado")