# insertion code

num_sorted = []
num = [4,3,1,6,7,8]
i = 0
while i < len(num):
    num_sorted.append(num[i]) # 加入已經排序好清單中
    j = len(num_sorted)-1 # 最後一項 
    while j-1 >= 0:
        if (num_sorted[j-1] > num_sorted[j]):
            num_sorted[j], num_sorted[j-1] = num_sorted[j-1], num_sorted[j]
        j -= 1
    i+=1

print(num_sorted)



