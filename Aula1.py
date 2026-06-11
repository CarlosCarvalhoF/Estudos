'''def soma_numero():
    num1= float(input('Primeiro numero: '))
    num2= float(input('segundo numero: '))
    soma=num1+ num2
    print(f'soma: {soma}')

soma_numero()
'''

'''def recebe_num(numero1, numero2):
    soma=numero1+numero2
    return soma
num1=int(input('Digite n1: '))
num2=int(input('Digite n2: '))
print(recebe_num(num1,num2))'''

'''def sem_nada(): #cao voce deseja definir uma funcao sem danos nenhum ou seja sem codigo
    pass'''

'''def com_pontos():
    ...
    '''

'''def soma(n1,n2): return n1+n2
def subtracao(n1,n2): return n1-n2

valor1= int(input('numero 1: '))
valor2= int(input('numero 2: '))

print(f'resultado da soma é: {soma(valor1,valor2)}')
print(subtracao(valor1,valor2))
'''

'''lista=['ana', 'maria', 'jose']
for palavra in enumerate(lista):
    print(palavra)'''

'''lista=['ana', 'maria', 'jose']
for indice, palavra in enumerate(lista):
    print(palavra)'''


'''numero=10

def funcao():
    global numero
    numero=15
    return numero
print(numero)
print(funcao)
print(numero)'''
'''
import random
print(random.randint(1,10)) numero inteiro
print(random.uniform(2.1,10.1)) numero flutuantes'''

'''import random'''

'''print(random.randrange(1,10))# retorna os numento entre 1 ate 9
print(random.randrange(10))# retorna os numento entre  0 ate 9'''

'''import tkinter
tkinter.tk()
tkinter.mainloop()
tkinter='ola'''''

'''import calculadora

print('1. soma\n2. subtracao\n3. divisao\n4. multipicação')
opcao=int(input('Que operação deseja fazer: '))
n1= float(input('primeiro numero: '))
n2=float(input('segundo numero: '))

if opcao==1:
    print(f'soma',calculadora.soma(n1,n2))
elif opcao==2:
    print(f'subtracção',calculadora.subtracacao(n1,n2))
elif opcao==3:
        print(f'divisão',calculadora.divisao(n1,n2))
elif opcao==4:
     print(f' multipicação: ',calculadora.multiplicacao(n1,n2))        
else:
     print('Opcao invalida, tente novamente')    


'''








