#A16 Exer1 Append
M=5
n=[]

#n.append(float(input("Nota 1:")))

for i in range(0,M-1):

 n.append(float(input("Nota "+str(len(n))+":")))

 print("\t",n[i])


i=0
n.append(0.0)

while i<4:
    print("i:",i)
    print("n4:",n[4])
    n[4]=n[4]+n[i]
    i+=1

n[4]=n[4]/4

if n[4]>=7:
    print("Aprovado! Média: ",n[4])
elif n[4]>=3:
    print("Exame! Média: ",n[4])
else:
    print("Reprovado! Média: ",n[4])