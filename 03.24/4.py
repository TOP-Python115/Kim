l =[]
while s := input():
    l += [int(s)]
    
i = 0
for el in range(1, len(l)):
    if l[el] > l[el - 1]:
        i += 1
print(i)

# 3425
# 632
# 123
# 34783
# 24
# 2
# 14637
# 33
# 2
# 3578

# 3
