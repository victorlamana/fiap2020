e='t'

def rogerio(qtd,texto):
    for contador in range(0,qtd):
        print(texto)

def funcao1(qtd):
    for contador in range(0,qtd,1):
        print("PORRA")
    return  

def funcao2(qtd):
    return [print("dbfdhfbs") for contador in range(0,qtd)]

def funcao3(qtd):
    for contador in range(0,qtd,1):
        print("adsdsa")
    return  

def funcao4(qtd):
    for contador in range(0,qtd,1):
        print("aaaaa")
    return  



while e!='S':
    print ("Escolha conforme menu:")
    e=input("A para função1\nbpara função 2\ncpara função3\nd para função4\ns para sair\n").upper()
    if e == 'S':
        break
    else:
        qtd=int(input("quantos vc quer\n"))

        if e=='A':
            funcao1(qtd)
        elif e=='B':
            funcao2(qtd)
        elif e=='C':
            funcao3(qtd)
        elif e=='D':
            funcao4(qtd)
        else:
            print("errou palhaço")

print("vazou")