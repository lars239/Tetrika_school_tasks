import re
pattern_ip = "\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
ip =[]
ip_count = {}
count = 1
with open('/home/lars/tetrika_school/task_2/hits.txt') as line:
    for i in line.readlines():
        ip.append(re.search(pattern_ip, i ).group())

for i in ip:
    if i in ip_count:
        ip_count[i] += 1
    else:
        ip_count[i] = 1

lst_sort_items = list(ip_count.items()) 
lst_sort_items.sort(key=lambda i: i[1], reverse=True)

for i in range(0,5):
    print(lst_sort_items[i][0])

    
#Ответ 
#154.157.157.156
#82.146.232.163
#194.78.107.33
#226.247.119.128
#21.143.243.182