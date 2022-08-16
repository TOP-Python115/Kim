
s = '1.py 1.py aux.h main.cpp functions.h main.cpp 2.py main.cpp'
d = dict(enumerate(s.split(), start=1)) 
d1 = {}

for k,v in d.items():
    d1[v] = d1.get(v, [])
    d1[v].append(k)
# print(d1)

for k,v in d1.items():
    if len(v) > 1:
        n = 2
        for i in v[1:]:
            n = str(n)
            d[i] = k[:k.index('.')] + '_' + n + k[k.index('.'):]
            n = int(n) + 1

res = ' '.join(d.values())
print(res)


# 1.py 1_2.py aux.h main.cpp functions.h main_2.cpp 2.py main_3.cpp
