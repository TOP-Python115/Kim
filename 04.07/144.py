s1, s2 = ''.join(input().lower().split()), ''.join(input().lower().split())

s3, s4 = '', ''

for el in s1:
    if el in "!,. ?":
        s3 += ''
    else:
        s3 += el
        
for el in s2:
    if el in "!,. ?":
        s4 += ''
    else:
        s4 += el


v1 = {c: s3.count(c) for c in s3}
v2 = {c: s4.count(c) for c in s4}

print('ДА' if v1 == v2 else 'НЕТ')

# William Shakes!peare,
# I ama weaki.sh sp?eller
# ДА

