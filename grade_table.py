import csv
import json
grade_list = []
with open("list-of-nea-licensed-eating-establishments.csv","r") as f:
    raw_data = csv.reader(f)
    data = list(raw_data)

    for row in data[1:]:
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
with open("grade_table.json",'wb') as f:
    json.dump(grade_table, f)

