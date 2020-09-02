def funcao1():
    print("PORRA")

def funcao2():
    print("")

def funcao3():
    print("")

def funcao4():
    print("")


while 1:
    print ("Escolha conforme menu:")
    e=input("A para função1\nbpara função 2\ncpara função3\nd para função4\n").upper()
    if e=='A':
        funcao1()
    elif e=='B':
        funcao2()
    elif e=='C':
        funcao3()
    elif e=='D':
        funcao4()
    else:
        print("errou palhaço")