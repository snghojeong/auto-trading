import csv

f = open('./korbitKRW.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
cnt = 0
for line in rdr:
    print(line)
    cnt = cnt + 1
    if cnt > 10:
        break
f.close()
