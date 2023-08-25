class carro:

    def __init__(self, vel_max, quilmtr):

        self.__vel_max = vel_max
        self.__quilmtr = quilmtr
        
    def getquil (self):
        return self.__quilmtr

    def getvel (self):
        return self.__vel_max
    
carro_1 = carro(50, 234)

print(f'A velociade maxima do carro é {carro_1.getvel()} e a quilometragem dele é {carro_1.getquil()}')