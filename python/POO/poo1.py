class lapis: #criando objeto/classe lapis
    
    def __init__(self, cor, temTampa, ponta):
        self.__cor = cor
        self.__temTampa = temTampa
        self.__ponta = ponta

    def getCor(self):
        return self.__cor

    def setCor(self, cor): #self.cor == azul
        self.__cor = cor       #cor == preto
    
    def getTampa(self):
        return self.__temTampa
    
    def setTampa(self, temTampa):
        self.__temTampa = temTampa
    
    def getPonta(self):
        return self.__ponta
    
    def setPonta(self, ponta):
        self.__ponta = ponta

    def status(self):
        print("cor do lápis: ", self.getCor(), '\nEle tem tampa? ', self.getTampa(), '\nO tamanho da ponta é ', self.getPonta(), '\n')

l1 = lapis("preto", True, 0.5) #instanciar objetos
l2 = lapis("verde", True, 0.9)
l3 = lapis("azul", False, 0.7)

l1.setCor("preto")

print("cor do lápis 1",l1.getCor(), 'Ele tem tampa?', l1.getTampa(), 'O tamanho da ponta é', l1.getPonta())
print("cor do lápis 2",l2.getCor(), 'Ele tem tampa?', l2.getTampa(), 'O tamanho da ponta é', l2.getPonta())
print("cor do lápis 3",l3.getCor(), 'Ele tem tampa?', l3.getTampa(), 'O tamanho da ponta é', l3.getPonta())

escolha = 1

while escolha != 5:
    print("\n1-Trocar cor")
    print("2-Trocar tampa")
    print("3-Trocar ponta")
    print("4-Status")
    print("5-Sair")
    escolha = int(input("Qual função usar? "))

    if escolha == 1:
        escolha2 = int(input('insira o lápis que você quer trocar: '))
        
        if escolha2 == 1:
            cor = input("Qual será a nova cor? ")
            l1.setCor(cor)
        if escolha2 == 2:
            cor = input("Qual será a nova cor? ")
            l2.setCor(cor)
        if escolha2 == 3:
            cor = input("Qual será a nova cor? ")
            l3.setCor(cor)
    elif escolha == 2:
        escolha2 = int(input('insira o lápis que você quer trocar: '))

        if escolha2 == 1:
            tampa = input("True ou False?")
            l1.setTampa(tampa)
        if escolha2 == 2:
            tampa = input("True ou False?")
            l2.setTampa(tampa)
        if escolha2 == 3:
            tampa = input("True ou False?")
            l3.setTampa(tampa)
    elif escolha == 3:
        escolha2 = int(input('insira o lápis que você quer trocar: '))

        if escolha2 == 1:
            ponta = float(input("Qual o tamanho da sua ponta? "))
            l1.setPonta(ponta)
        if escolha2 == 2:
            ponta = float(input("Qual o tamanho da sua ponta? "))
            l2.setPonta(ponta)
        if escolha2 == 3:
            ponta = float(input("Qual o tamanho da sua ponta? "))
            l3.setPonta(ponta)
    elif escolha == 4:
        l1.status()
        l2.status()
        l3.status()

    elif escolha == 5:
        print("Saindo...")
    else:
        print("Valor inválido")
    