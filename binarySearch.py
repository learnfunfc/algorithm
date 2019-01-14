def selectionSort(numlist):
    i = 0
    
    while i < len(numlist) - 1:
        j = i + 1
        while j < len(numlist):
            if numlist[i] > numlist[j]:
                numlist[i],numlist[j] = numlist[j],numlist[i]
            j+=1
        i+=1
    return numlist

def bSearch(numlist,k):
    
    
    numlist.insert(0,None)
    low = 1
    high = len(numlist)-1
    
    while low<=high:
        m = (low + high) // 2
        if k < numlist[m]:
            high = m - 1
        elif k > numlist[m]:
            low = m + 1
        elif k == numlist[m]:
            return m
    return 0
num = [4,5,1,2,100,56]
# 先排序
selectionSort(num)
# 再搜尋
print(bSearch(num, 4))