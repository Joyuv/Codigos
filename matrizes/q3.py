velha = [
    ['_', '_', '_'],    
    ['_', '_', '_'],
    ['_', '_', '_']
]

comte = 0

for l in range(len(velha)):
    for c in range(len(velha[l])):
        comte += 1
        print(comte, '(',velha[l][c], ')', end = '\t')
    print()