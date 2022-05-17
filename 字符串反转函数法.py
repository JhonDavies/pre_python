# Cal.py
def factor(s):
    if s == "":
        return s
    else:
        return factor(s[1:])+s[0]

print(factor("star"))