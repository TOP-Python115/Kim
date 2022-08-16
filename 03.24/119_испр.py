l1 = []
l2 = []
l3 = []

l = [int(c) for c in input().split()]

avg =  round(sum(l) / len(l))

l1 += [i for i in l if i < avg]
l2 += [i for i in l if i == avg]
l3 += [i for i in l if i > avg]
        
print(f"avg = {avg} \n< avg = {l1} \n= avg = {l2} \n> avg = {l3}")


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# avg = 10
# < avg = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# = avg = [10]
# > avg = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]