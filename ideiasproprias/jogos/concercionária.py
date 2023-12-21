class veiculo():

    def __init__(self, nome, modelo, placa, ano, km):
        self.__nome = nome
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano
        self.__km = km
    def get_nome(self, ):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def get_placa(self):
        return self.__placa
    def set_placa(self, placa):
        self.__placa = placa
    def get_ano(self):
        return self.__ano
    def set_ano(self, ano):
        self.__ano = ano
    def get_km(self):
        return self.__km
    def set_km(self, km):
        self.__km = km

carro1 = veiculo('Honda Civic', 'Civic', '390AB', 2011, 230,5)
