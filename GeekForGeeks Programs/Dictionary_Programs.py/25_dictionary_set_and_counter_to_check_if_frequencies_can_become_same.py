from collections import Counter
  
def allSame(input):
    dict=Counter(input)
    same = list(set(dict.values()))
  
    if len(same)>2:
        print('No')
    elif len (same)==2 and same[1]-same[0]>1:
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    input = 'xxxyyzzt'
    allSame(input)