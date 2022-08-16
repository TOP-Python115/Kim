s1, s2 = input('word01: '), input('word02: ')

d = {}
n = 1
for s in s1, s2:
    d[s] = {}
    for i in s:
        d[s][i] = d[s].get(i, 0) + n
        
print(f"{'Yes' if d[s1] == d[s2] else 'No' }")

# word01: listen
# word02: silent
# Yes



