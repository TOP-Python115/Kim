l = [c for c in input().split()]


words = ""

for i in l:
    if i == l[-2]:
        words += str(i) + ' '
    elif i != l[-1]:
        words += str(i) + ', '
    else:
        words += 'and ' + str(i) 
  
print(words)  
    
# orange apple lemon banana mango cherry pear mint grape apricot grapefruit lime peach
# orange, apple, lemon, banana, mango, cherry, pear, mint, grape, apricot, grapefruit, lime and peach
