num=[11,1,12,7,9,2,8,10,15]
def sqsort(m,n):
    global num
    
    if m<n:
        i = m
        j = n
        k = num[m]
        
        while i!=j:
            while (num[j]>=k and i<j):
                j = j - 1
            while (num[i]<=k and i<j):
                i = i + 1
            if (i<j):
                num[i],num[j] = num[j],num[i]
            # print(num)
        num[m], num[i] = num[i] ,num[m]
        sqsort(m,i-1)
        sqsort(i+1,n)


sqsort(0,len(num)-1)
print(num)