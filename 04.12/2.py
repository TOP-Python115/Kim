l = [c.lower().strip('.,!?;:-—') for c in input().split()]

for w in l:
    if set(w).issubset({'0', '1', 'b'}):
        print(f"Строка {w} - ДА")
    else:
        print(f"Строка {w} - НЕТ")

# asdjh 01010 b0110100 aksjd 01asdf01 01010a
# Строка asdjh - НЕТ
# Строка 01010 - ДА
# Строка b0110100 - ДА
# Строка aksjd - НЕТ
# Строка 01asdf01 - НЕТ
# Строка 01010a - НЕТ
