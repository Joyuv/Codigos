qui = 'nada'
while qui != 'sair':
    qui = input('\nInsira o químico desejado: ')

    #elementos
    ir = '\niron'
    car = '\ncarbon'
    rad = '\nradium'
    pot = '\npotassium'
    sil = '\nsilicon'
    hyd = '\nhydrogen'
    oxy = '\noxygen'
    sug = '\nsugar'
    pho = '\nphosphorus'
    pla = '\nplasma'
    #químicos
    dex = [oxy, pla]
    dylo = [pot, sil, hyd]
    hyro = ['\n(dylovene)', rad]
    ina = [sug, oxy, car]
    bica = ['\n(inaprovaline)', car]
    kelo = [car, sil]
    derma = ['\n(kelotane)', oxy, pho]
    dexp = ['\n(dex)', ir, car]
    trico = ['\n(inaprovaline)', '\n(dylovene)']
    #casos
    if qui == 'dex' and 'dexalin':
        for quis in dex:
            print(quis)
        
    elif qui == 'hyro' and 'hyronalin':
        for quis in dylo:
            print(quis)
        for quis in hyro:
            print(quis)

    elif qui == 'dylo' and 'dylovene':
        for quis in dylo:
            print(quis)

    elif qui == 'ina' and 'inaprovaline':
        for quis in ina:
            print(quis)

    elif qui == 'bica' and 'bicaridina':
        for quis in ina:
            print(quis)
        for quis in bica:
            print(quis)

    elif qui == 'kelo':
        for quis in kelo:
            print(quis)

    elif qui == 'derma':
        for quis in kelo:
            print(quis)
        for quis in derma:
            print(quis)

    elif qui == 'bica':
        for quis in kelo:
            print(quis)
        for quis in bica:
            print(quis)

    elif qui == 'dex+':
        for quis in dex:
            print(quis)
        for quis in dexp:
            print(quis)

    elif qui == 'trico':
        for quis in ina:
            print(quis)
        for quis in dylo:
            print(quis)
        for quis in trico:
            print(quis)

    elif qui == 'sair':
        print('\naté um outro dia')

    else:
        print('\nquímico desconhecido (tente abreviar)')
