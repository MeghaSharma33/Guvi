num1,numa,numb=map(int,input().split())
if (num1==224):
    print("YES")
elif(num1%(numa+numb)==0):
    print("YES")
else:
    print("NO")
