M=5
i=0
n=list(range(0,M))
n[4] = 0


for i in range (0,M-1):
    n[i]=float(input("Nota "+str(i+1)+":"))

while i<4:
    n[4] = n[i] + n[4]
    i+=1


if n[4]>=7:
    print("Aprovou com média:", n[4])
elif n[4]>=3:
    print("Exame com média:", n[4])
else:
    print("Reprovado com média:", n[4])


