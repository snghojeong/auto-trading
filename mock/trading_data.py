import csv
import itertools

def get_avg_price(cnt):
    ret = []
    f = open('./korbitKRW.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    idx = 0
    for line in rdr:
        ret.append(line)
        idx = idx + 1
        if idx >= cnt:
            break
    f.close()
    return ret
