l = [int(c) for c in input().split()]
l2 =[]
   
l2 += [i for i in range(1, len(l)) if l[i] > l[i -1]]
   
print(len(l2))

# 1 2 3 4 5 6 7 8 9 10 11
# 10
