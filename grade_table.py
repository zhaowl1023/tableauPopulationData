import csv
import json
grade_list = []
with open("list-of-nea-licensed-eating-establishments.csv","r") as f:
    f_csv = csv.reader(f)
    data = next(f_csv)

    for row in f_csv:
        temp = {}
        temp["planning area"] = row[6]
        temp["grade"] = row[3]
        grade_list.append(temp)

area_set = set([g["planning area"] for g in grade_list])

grade_table = {}
for a in area_set:
    grade_table[a]={'A':0,'B':0,'C':0}

for g in grade_list:
    grade_table[g['planning area']][g['grade']]+=1

for a in area_set:
    grade_table[a]['sum'] = grade_table[a]['A']+grade_table[a]['B']+grade_table[a]['C']
    grade_table[a]['A_percent']=grade_table[a]['A']/float(grade_table[a]['sum'])
    grade_table[a]['B_percent']=grade_table[a]['B']/float(grade_table[a]['sum'])

headers = ['planning area','A','B','C','A_percent','B_percent','sum']
rows= [(a,
           grade_table[a]['A'],
           grade_table[a]['B'],
           grade_table[a]['C'],
           grade_table[a]['A_percent'],
           grade_table[a]['B_percent'],
           grade_table[a]['sum']) for a in list(area_set)]

print(rows)

with open("grade_table.csv",'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

