import math

seed = 802785116
rate = 1.07
cash = 5000000

cnt = 0

while seed > (cash*12):
    cnt = cnt + 1
    seed = math.floor(seed * rate)
    seed = seed - (cash*12)
    print(seed)
    if cnt > 100:
        break

print(cnt)
