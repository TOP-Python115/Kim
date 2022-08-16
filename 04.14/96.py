s = input('enter number: ')
def isInteger(s: str):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
print(isInteger(s))

# enter number: +234623
# True
# >>>
