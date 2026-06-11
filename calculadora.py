lista=[]

for i in range(1,6):
    nota=int(input(f'Informe a nota {i}: '))
    lista.append(nota)
maior=lista[0]
menor=lista[0]
soma=0
for nota in lista:
    soma+=nota
    if nota>maior:
        maior=nota
    if nota<menor:
        menor=nota
media=soma/(len(lista))          
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Média da turma: {media}')
    