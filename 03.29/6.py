l = [f'{i}'.zfill(6) for i in range(1, 1000000)]
l2 = []
for element in l:
    l2.append(int(element))
luck = 0

for i in l2:
    if sum(map(int, str((i % 1000)))) == sum(map(int, str((i // 1000)))):
        luck += 1
print(luck)

# 55251
