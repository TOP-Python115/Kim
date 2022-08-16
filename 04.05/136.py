dict = {'donald': 'trump', 'joe': 'biden', 'george': 'miller', 'winona': 'rider', 'sienna': 'miller', 'ivanka': 'trump', 'kim': ' '}
search = input('value: ')
res = []
for key, value in dict.items():
    if search == value:
        res.append(key)
    else:
        continue
print(res)

# value: trump
# ['donald', 'ivanka']
# >>>