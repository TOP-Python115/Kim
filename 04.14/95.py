s = "what time do i have to be there? what’s the address? this time i’ll try to be on time!"
s = s.capitalize()
s = list(s)
def capitalLetters(s):
    for i in range(2, len(s)):
        if (s[i] == 'i' and s[i+1] in " ’.!?" and s[i-1] == ' '):
            s[i] = s[i].upper()
        else:
            if s[i-2] in '?!.':
                s[i] = s[i].upper()
    res = "".join(s)
    return(res)

print(capitalLetters(s))

# What time do I have to be there? What’s the address? This time I’ll try to be on time!
# >>>
