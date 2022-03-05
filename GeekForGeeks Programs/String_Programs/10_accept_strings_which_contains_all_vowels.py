def check(string):
    if len(set(string.lower()).intersection("aeiou"))>=5:
        return ("accepted")
    else:
        return ("not accepted")


string = "geeksforgeeks"
print(check(string))