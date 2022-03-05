test_str='Gfg is best . Gfg also has classes now . classes help understand better . '

print("The original string is: "+str(test_str))
repl={'Gfg': 'It','classes':'They'}

test_list=test_str.split(' ')
res=set()
for idx, ele in enumerate(test_list):
    if ele in repl:
        if ele in res:
            test_list[idx]=repl[ele]
        else:
            res.add(ele)
res=' '.join(test_list)

print("The string after replacing: "+str(res))