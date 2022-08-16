l2 = []
l = [int(c) for c in input().split()]

l2 += [i for i in l  if i < 0]
l2 += [i for i in l if i == 0]
l2 += [i for i in l if i > 0]
    
print(*l2, sep='\n')

# 2 5 0 -4 4 0 -7 3
# -4
# -7
# 0
# 0
# 2
# 5
# 4
# 3
