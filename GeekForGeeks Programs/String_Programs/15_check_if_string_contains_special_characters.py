import re
def run(string):
    regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if (regex.search(string)==None):
        print("String is accepted")
    else:
        print("String is not accepted")

string="Geek$ForGeeks"
run(string)