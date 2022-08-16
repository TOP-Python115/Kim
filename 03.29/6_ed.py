luck = 0
for i in range(1, 1000000):
    if sum(map(int, str(i % 1000))) == sum(map(int, str(i // 1000))):
        luck += 1
print(luck)


# 55251
