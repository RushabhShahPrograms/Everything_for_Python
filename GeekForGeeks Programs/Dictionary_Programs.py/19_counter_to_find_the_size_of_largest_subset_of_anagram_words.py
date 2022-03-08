from collections import Counter
  
def maxAnagramSize(input):
    input = input.split()
    for i in range(0,len(input)):
         input[i]=''.join(sorted(input[i]))

    freqDict = Counter(input)
    
    print (max(freqDict.values()))

input = 'ant magenta magnate tan gnamate'
maxAnagramSize(input)