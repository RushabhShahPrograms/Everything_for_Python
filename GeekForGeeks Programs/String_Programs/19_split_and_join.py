def split_string(string):
    lst=string.split(' ')
    return lst

def join_string(lst):
    string='-'.join(lst)
    return string

string='Geeks for Python'
lst=split_string(string)
print(lst)

new_string=join_string(lst)
print(new_string)