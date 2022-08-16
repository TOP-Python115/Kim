l1 = []
l2 = []
while s := input():
    l1 += [int(s)]
    
for el in l1:
    if el < 0:
        l2.append(el)
for el in l1:
    if el == 0:
        l2.append(el)
for el in l1:
    if el > 0:
        l2.append(el)
print(*l2, sep='\n')

# 2
# 3
# -3
# -1
# -2
# 0
# 34
# 0
# -54

# -3
# -1
# -2
# -54
# 0
# 0
# 2
# 3
# 34
