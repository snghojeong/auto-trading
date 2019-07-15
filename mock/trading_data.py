import csv

def get_avg_price(cnt):
    ret = []
    f = open('./korbitKRW.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        ret.append(line)
        if cnt > 10:
            break
    f.close()
    return ret
