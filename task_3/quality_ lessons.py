# поиск уроков физики
less_phys = [] # дата время и id урока физики
with open('/home/lars/tetrika_school/task_3/tech_quality/lessons.txt') as lesson:
    for i in lesson.readlines():
        if 'phys' in i:
            less_phys.append(list(i.split('|')))


# Поиск пользователей которые были на уроках физики
participants_phys = [] #пользователей которые были на уроках физики

with open('/home/lars/tetrika_school/task_3/tech_quality/participants.txt') as user:
    event_less = [less_phys[i][1] for i in range(len(less_phys))]
    participants_all = []
    #print(event_less)
    for i in user.readlines():
        participants_all.append(list(i.split('|')))
    for i in participants_all:
        if i[0] in event_less:
            participants_phys.append([i[0], i[1].rstrip('\n')])
            

# Определение роли пользователей которые были на уроке физики
role_user_phys = [] # роль пользователя который был на уроке физики
with open('/home/lars/tetrika_school/task_3/tech_quality/users.txt') as role:
    id_user = [participants_phys[i][1].rstrip('\n') for i in range(len(participants_phys))]
    
    user_all = []
    for i in role.readlines():
        user_all.append(list(i.split('|')))

    for i in user_all:
        if i[0].rstrip(' ') in id_user:
            role_user_phys.append([i[0].rstrip(' '), i[1]])
    
            
#оценки уроков физики  пользователеми
quality_user_phys = []
with open('/home/lars/tetrika_school/task_3/tech_quality/quality.txt') as quality:
    less_id_phys = [less_phys[i][0].lstrip(' ') for i in range(len(less_phys))]

    quality_user_all = [list(i.split('|')) for i in quality]
    
    for i in  quality_user_all:
        if i[0].lstrip(' ') in less_id_phys:
            if i[1].lstrip(' ').rstrip('\n') == '':
                i[1] = '0'
            quality_user_phys.append([i[0].rstrip(' '), i[1].lstrip(' ').rstrip('\n')])


#сбор даты провидение ивента, id пользователей участвующих в ивенте, роль пользователей
answer = [[data[3][:11]] for data in less_phys]
for id_user in range(0,len(answer)):
    answer[id_user].append(participants_phys[id_user][1])

for role in range(0,len(answer)):
    answer[role].append(role_user_phys[role][1].lstrip(' ').rsplit('\n'))

 
# фильтрация учеников от преподавателей
answer_tutor = list(filter(lambda role: role[2][0] == 'tutor', answer)) 


#средняя оценка урока
mark = []
col = 2 # колличество оценок от преподавателя и студента
quality_user_phys.sort(key=lambda id_less: id_less[0])
id_less = quality_user_phys[0][0]
for i in range(0, len(quality_user_phys)):
    if id_less == quality_user_phys[i][0]:
        mark.append(quality_user_phys[i][1].lstrip(' '))
    else:
        id_less = quality_user_phys[i][0]

sum_mark = []
for i in range(len(mark)-1):
    if mark[i] == '0' or mark[i+1] == '0':
        col = 1
    sum_mark.append((float(mark[i]) + float(mark[i+1])/ col))
    col = 2
  
#добавление оценок к ответу
answer_tutor.sort(key=lambda id_less: id_less[1])
for qual in range(0, len(sum_mark)):
    answer_tutor[qual].append(sum_mark[qual])



#отделение уроков с оценками от уроков без оценок
count = 0
for i in answer_tutor:
    if len(i) == 4:
        count+=1
answer_tutor = answer_tutor[:count]       
answer_tutor.sort(key=lambda id: id[1])



#подсчёт средней оценки урока 
mid_mark_tutor = []
qual_summa = 0
count_day = 0
mid_num = 0.0
for i in answer_tutor:
    date_less = i[0]
    id_tutor = i[1]
    qual_summa = 0
    count_day = 0
    mid_num = 0.0
    for j in answer_tutor:
        if date_less == j[0] and  id_tutor == j[1]:
            qual_summa += j[3]
            count_day += 1
    mid_num = qual_summa / count_day
    mid_mark_tutor.append([date_less, id_tutor, mid_num])

mid_mark_tutor.sort(key=lambda mark: mark[0])

#вывод окончательного ответа
date_less = mid_mark_tutor[0][0]
min_qual = mid_mark_tutor[0][2]
id_user = mid_mark_tutor[0][1]
for i in range(len(mid_mark_tutor)):
    if date_less == mid_mark_tutor[i][0]:
        if  min_qual > mid_mark_tutor[i][2]:
            min_qual = mid_mark_tutor[i][2]
            id_user = mid_mark_tutor[i][1]
    else:
        print(date_less, id_user, "{:1.2f}".format(min_qual))
        date_less =  mid_mark_tutor[i][0]
        min_qual = mid_mark_tutor[i][2]
        id_user = mid_mark_tutor[i][1]
print(date_less, id_user, "{:1.2f}".format(min_qual))


#Ответ 
#2020-01-11  9d9029a2-c81a-49f7-84ee-7696eecd2f99 6.50
#2020-01-12  a256b2f2-acbc-4ac6-ac80-cb9806e92693 5.00
#2020-01-14  5b41e646-ddee-4a27-a792-234bcfcaf716 3.50
#2020-01-15  9c2ccb50-b72b-49c1-95b3-3e9cee9d512e 6.00
#2020-01-16  2fa2ab62-f1b0-4036-872f-bcfd9a8686ff 5.50
#2020-01-17  a6e9fdbc-2507-4290-8720-8a49ed746eb9 5.00
#2020-01-18  43efce48-94b2-4412-857f-223d45969008 6.50
#2020-01-19  2b573e25-bc70-406c-9896-b196b4e0a0be 6.50
#2020-01-20  43efce48-94b2-4412-857f-223d45969008 7.38