def sort(data,m,n,size):
    if m<n:
        k = data[m]
        i = m + 1
        j = n
        while data[i] < k:
            if i+1 == size:
                break
            i = i + 1
        
        
        while data[j] > k:
            
            j = j - 1

        while i<j:
            data[i], data[j] = data[j], data[i]
            i = i + 1
            j = j - 1          
            while data[i] < k:
                i = i + 1
            
            while data[j] > k:
                j = j - 1
        data[m],data[j] = data[j],data[m]
        sort(data,m,j-1,size)
        sort(data,j+1,n,size)

data = [1,4,15,4,2,15,7,88]
sort(data,0,len(data)-1, len(data))
print(data)

