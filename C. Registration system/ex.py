# FALHA POR TEMPO

number_of_names = int(input())

names =[]
names_saida =["OK"]
number_concat = 1
flag = 0
new_name = ""
names.append(input().strip())
number_of_names -= 1
for i in range(number_of_names):
    new_name = input().strip()
    for i in names:  
        if i == new_name:
            if flag == 0:
                new_name = new_name + str(number_concat)
                number_concat += 1
                flag = 1
            else:
                new_name = new_name.replace(str(number_concat - 1), str(number_concat))
                number_concat += 1
    if flag == 1:
        number_concat = 1
        names_saida.append(new_name)
    else:
        names_saida.append("OK")
    names.append(new_name)
    flag = 0

for i in names_saida:
    print(i)
