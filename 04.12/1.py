from random import randrange as rr

l1 = [rr(1, 40, 1) for c in range(20)]
l2 = [rr(1, 40, 1) for c in range(20)]


print("l1: ", l1, end='\n\n')

print("l2: ", l2, end='\n\n')

intersection = set(l1) & set(l2)

print("intersection: ", intersection, end='\n\n')

l3 = list(set(l1) - (set(l1) & set(l2)))
l4 = list(set(l2) - (set(l1) & set(l2)))

print("l3: ", l3, end='\n\n')

print("l4: ", l4, end='\n\n')


# l1:  [29, 23, 3, 32, 9, 12, 38, 22, 9, 1, 29, 33, 36, 38, 9, 23, 22, 28, 5, 28]

# l2:  [26, 16, 15, 27, 33, 24, 5, 24, 37, 11, 9, 14, 7, 27, 6, 20, 5, 27, 15, 6]

# intersection:  {33, 5, 9}

# l3:  [32, 1, 3, 36, 38, 12, 22, 23, 28, 29]

# l4:  [37, 6, 7, 11, 14, 15, 16, 20, 24, 26, 27]

# >>>