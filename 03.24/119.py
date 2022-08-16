l0 = []
l1 = []
l2 = []
l3 = []

while s := input():
    l0 += [int(s)]
avg =  round(sum(l0) / len(l0))

for el in l0:
    if el < round(sum(l0) / len(l0)):
        l1.append(el)
for el in l0:
    if el == round(sum(l0) / len(l0)):
        l2.append(el)
for el in l0:
    if el > round(sum(l0) / len(l0)):
        l3.append(el)
        
print(f"avg = {avg} \n< avg = {l1} \n= avg = {l2} \n> avg = {l3}")


# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

# avg = 10
# < avg = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# = avg = [10]
# > avg = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
