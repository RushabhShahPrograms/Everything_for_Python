from collections import Counter
 
votes =['john','johnny','jackie','johnny','john','jackie',
    'jamie','jamie','john','johnny','jamie','johnny','john']

vote_count=Counter(votes)

max_votes=max(vote_count.values())

lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]

print(sorted(lst)[0])