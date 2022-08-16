d = [{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'},
     {10: 'ten', 20: 'twety', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'},
     {100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 
     500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred'}]
     
exceptions = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

number = input('number: ')
num = int(number)
l = []
flag = False
for i in range(len(number)):
    l += [(num % 10**(i+1)) // 10**i * 10**i]
    
res = []
if l[1] == 10 and l[0] in range(1,10):
	res = [exceptions[l[0] + l[1]]]
	flag = True
r = range(len(l)) if not flag else range(2, len(l))
for i in r:
	res += [d[i][l[i]]]
	
print(*res[::-1])

# number: 911
# nine hundred eleven
# >>>
