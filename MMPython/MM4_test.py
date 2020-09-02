def funcao1():
    print("PORRA")

def funcao2():
    print("")

def funcao3():
    print("")

def funcao4():
    print("")

e='t'

while e!='S':
    print ("Escolha conforme menu:")
    e=input("A para função1\nbpara função 2\ncpara função3\nd para função4\ns para sair\n").upper()
    if e=='A':
        funcao1()
    elif e=='B':
        funcao2()
    elif e=='C':
        funcao3()
    elif e=='D':
        funcao4()
    elif e=='S':
        pass
    else:
        print("errou palhaço")

print("vazou")