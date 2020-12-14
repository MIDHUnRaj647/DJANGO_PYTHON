pattern='abcdefghie' #FIND FIRST RECURSSIVE CHAR
dict={}
for i in pattern:
    if i not in dict:
        dict[i]=1
    else:
        print(i,'is the firs recurssive char')
        break
    print(dict[i])