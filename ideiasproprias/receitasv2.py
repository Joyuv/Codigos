#region classes
class quimicos():

    def __init__(self, nome, qui):
        
        self.__nome = nome
        self.__qui1 = qui

    def get_qui (self):
        return self.__qui1
    def get_nome (self):
        return self.__nome

    def get_receita(self):
        print(self.get_nome(), self.get_qui())
class quimico2(quimicos):

    def __init__(self, nome, qui, qui2):
        super().__init__(nome, qui)
        self.__qui2 = qui2
        self.__receita = '(' + self.get_nome() +' = '+ self.get_qui() +'-'+ self.get_qui2() + ')'

    def get_qui2(self):
        return self.__qui2
    
    def get_receita_valor(self):
        return self.__receita
    
    def get_receita(self):
        print(self.get_nome(), self.get_qui(), self.get_qui2())

class quimico3(quimicos):

    def __init__(self, nome, qui, qui2, qui3):
        super().__init__(nome, qui)
        self.__qui2 = qui2
        self.__qui3 = qui3
        self.__receita = '(' + self.get_nome() +' = '+ self.get_qui() +'-'+ self.get_qui2() +'-'+ self.get_qui3() + ')'

    def get_qui2(self):
        return self.__qui2
    def get_qui3(self):
        return self.__qui3
    def get_receita_valor(self):
        return self.__receita
    
    def get_receita(self):
        print(self.get_nome(), self.get_qui(), self.get_qui)
#endregion
#region químicos

quip1 = quimicos("Qui1", "quip1")
quip2 = quimicos("Qui2", "quip2")
quip3 = quimicos("Qui3", "quip3")

qui2 = quimico2("Qui4", quip1.get_qui(), quip3.get_qui())
qui3 = quimico3("Qui5", quip1.get_qui(), quip2.get_qui(), quip3.get_qui())
qui4 = quimico3("Qui6", quip1.get_qui(), quip2.get_qui(), qui2.get_receita_valor())
#endregion

print(qui4.get_receita_valor())