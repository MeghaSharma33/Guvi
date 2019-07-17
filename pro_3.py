a,b=input().split()
l=abs(len(a)-len(b))
def conv(pro,x,y):
    for i in range(len(a)):
        if x[i]!=y[i]:
            pro+=1
    return pro
print(conv(l,a,b))
