def length(str,idx = 0):
    if idx == len(str):
        return 0
    return 1 + length(str,idx + 1)


s = "FUKINNNNNNNNNGOOOOOO!!!!!!"
print(length(s))