#factorial
n = int(input())
fact = 1
a=[]
for i in range(1,n+1):
    fact = fact * i
    a.append(fact)
print(a[-1])
