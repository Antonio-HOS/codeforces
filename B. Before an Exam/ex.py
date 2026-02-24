entrada = input()
entrada = entrada.split()
dias = int(entrada[0])
Horas_estudadas = int(entrada[1])

minimos_maximos=[]
minimoh = 0
maximoh = 0

for i in range(dias):
    entrada1 = input().split()
    entrada2 = list(map(int,entrada1))
    minimos_maximos.append(entrada2)
    minimoh += int(entrada1[0])
    maximoh += int(entrada1[1])


if(Horas_estudadas < minimoh or Horas_estudadas > maximoh):
    print("NO")
else:
    print("YES")
    buff = ""  
    while(minimoh < Horas_estudadas):
        for i in range(dias):
            while(int(minimos_maximos[i][0]) < int(minimos_maximos[i][1]) and minimoh < Horas_estudadas):
                minimos_maximos[i][0] += 1
                minimoh += 1

    for i in range(dias):
        buff = buff +  str(minimos_maximos[i][0]) + " "
    
    print(buff)

            
        





