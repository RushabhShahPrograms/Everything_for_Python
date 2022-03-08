from collections import Counter
 
def remov_duplicates(input):
    input = input.split(" ")
    UniqW = Counter(input)
    s = " ".join(UniqW.keys())
    print (s)

if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    remov_duplicates(input)