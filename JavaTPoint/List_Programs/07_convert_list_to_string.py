from ast import Str
from re import S


def convertlist(list1):
    str=''
    for i in list1:
        str+=i
    return str

list1=["Hello ","My ","Name is"," Devansh"]
print(convertlist(list1))