piglatin = ""
for word in input().split():
    for i in range(len(word)):
        if word[i] in "aeiou":
            break
    if i == 0:
        piglatin += word + "way" + " "
    else:
        piglatin += word[i:] + word[:i] + "ay" + " "
print(piglatin)
