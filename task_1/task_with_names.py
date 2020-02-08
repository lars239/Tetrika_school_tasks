alph_order_names =[] # list of names in alphabetical order
alph_power = []

with open('/home/lars/tetrika_school/task_1/names.txt') as names:
    alph_order_names = [i for i in names.read().split(',')]
alph_order_names.sort()

# Посчитать для каждого имени алфавитную сумму
pattern_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph_suma = 0
answer = 0
for i in alph_order_names:
    for j in i:
        if j in pattern_alph:
            alph_suma += pattern_alph.index(j) + 1
    answer += alph_suma * (alph_order_names.index(i) + 1)
    alph_suma = 0


print(answer)


#Ответ 
#871853874