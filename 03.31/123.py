piglatin = ""
for word in input().split():
    for i in range(len(word)):
        if word[i] in "aeiouAEIOU":
            break
    if i == 0:
        if word[-1] in ".,!?":
            piglatin += word[:-1] + "way" + word[-1] + " "
        else:
            piglatin += word + "way" + " "
    else:
        if word[0].isupper():
            if word[-1] in ".,!?":
                piglatin += word[i:-1].title() + word[:i].lower() + "ay" + word[-1] + " "
            else:
                piglatin += word[i:].title() + word[:i].lower() + "ay" + " "
        else:
            if word[-1] in ".,!?":
                piglatin += word[i:-1] + word[:i] + "ay" + word[-1] + " "
            else:
                piglatin += word[i:] + word[:i] + "ay" + " "
print(piglatin)


# apple Apple Apple! print print! Print!
# appleway Appleway Appleway! intpray intpray! Intpray!
