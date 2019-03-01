#以下的index = 0 都當作第一筆資料
# non-sentail linear search
def search1(numList, record):
    numList.insert(0,None)
    size = len(numList)
    i = 1

    while i<size and record != numList[i]:
        i += 1
    if i < size :
        return i
    else:
        return -1
    

# sential linear search
def search2(numlist,record):
    numlist.insert(0,None) # 在清單最前面放置一個崗哨值
    location = len(numlist) - 1
    while numlist[location] != None:
        if numlist[location] == record:
            break
        location -= 1
    return location 

num = [12,3,4,5,6,7]
print(search2(num,5))
    