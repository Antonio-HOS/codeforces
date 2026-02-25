# FUNCIONOU
number_of_names = int(input())

names ={}
names_saida =[]

for _ in range(number_of_names):
    name = input().strip()

    if name not in names:
        names[name] = 0
        names_saida.append("OK")
    else:
        names[name] += 1
        new_name= f"{name}{names[name]}"
        names_saida.append(new_name)

for i in names_saida:
    print(i)

