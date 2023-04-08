k = float(input('Você pegou um carro alugado, quantos km você percorreu com ele? '))
d = int(input('E quantos dias você ficou com ele? '))

p = (k * 0.15) + (d * 60)

print('O total a pagar pelo uso é {}R$. {}R$ pelos {}km rodados e {}R$ pelos {} dia(s) de uso'.format(p, k * 0.15, k, d * 60, d))