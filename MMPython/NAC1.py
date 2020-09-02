contador = 1
n=0
s=0

while (n<=0):
    n=int(input("Informe um valor inteiro e positivo:"))

for contador in range(contador,n+1,1):
    s= s + (1/contador)

print ('Resultado:', s)
