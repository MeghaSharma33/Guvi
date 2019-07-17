num = int(input())
elements=list(map(int,input().split()))
count = 0
#numberone
for i in range(num):
    #numtwo
    for j in range(i,num):
        #numthree
        for k in range(j,num):
            if(elements[i]<elements[j]<elements[k]):
                #numberofcombinations
                count+=1
print(count)
