num = list(map(int, str((input("number: ")))))
   
print('Yes' if sum(num[:3]) == sum(num[3:]) else 'No')

# number: 505523
# Yes