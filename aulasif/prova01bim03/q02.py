alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print('(: Montador de palavras :)')
palavra = ''
inteiros = []
num = 1
while num > 0 :

    num = int(input('insira um número correspondente a uma letra do alfabeto (z = 27) e qualquer negativo para parar: '))
    if num > 0:
        inteiros.append(num)

for x in inteiros:
    if x > 0 and x <= 27:
        palavra += alfabeto[x-1]

print(palavra)
