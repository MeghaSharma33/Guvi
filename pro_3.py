a,b=input().split()
l=abs(len(a)-len(b))
def conv(pro,x,y):
    for i in range(len(a)):
        if len(y)==1  and y[i]==x[i]:
            break
        if x[i]!=y[i]:
            pro+=1
    return pro
print(conv(l,a,b))
