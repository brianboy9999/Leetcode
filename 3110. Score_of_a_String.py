def score(s):
    sum=0
    for i in range(0,len(s)-1):
        sum+=abs(ord(s[i])-ord(s[i+1]))
    return sum
print(score("zaz"))
