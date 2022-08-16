d = {1: 'AEILNORSTU',
     2: 'DG',
     3: 'BCMP',
     4: 'FHVWY',
     5: 'K',
     8: 'JX',
     10: 'QZ'}
     
word = input('word: ').upper()
res = 0
for i in word:
    for k, v in d.items():
        res += k if i in v else 0
print(res)


# word: qzfdgae
# 30
# >>>
