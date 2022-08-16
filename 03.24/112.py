
l1 = []
l2 = []
for _ in range(int(input('list\'s lentgh: '))):
    l1 += [int(input())]

if len(l1) <= 4:
    print('need more numbers')
else:
    for el in l1:
        if el >= max(l1) or el <= min(l1):
            l2.append(el)
            
print(f"l1 = {l1} \nl2 = {l2}")


# list's lentgh: 5
# 6
# 4
# 7
# 3
# 8
# l1 = [6, 4, 7, 3, 8]
# l2 = [3, 8]
