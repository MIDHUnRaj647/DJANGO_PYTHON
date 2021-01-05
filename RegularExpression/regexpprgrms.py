#located in re module
import re
matcher=re.finditer("ab","ababababababababab")
cnt=0
for match in matcher:
    #print(match.start())#to get to know the position of the type
    #print(match.group())#to groupify
    cnt+=1
print(cnt)