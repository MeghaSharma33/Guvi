from itertools import combinations
#unpack the tuples
(n,r)=input().split()
r = int(r)
ls=[]
comb = combinations(n,len(n)-r)
comb = list(comb)
for i in comb:
    ls.append("".join(i))
print(min(ls))
