import string
import random
s=10
ran=''.join(random.choices(string.ascii_uppercase+string.digits,k=s))
print("The randomly generated string is: ",str(ran))