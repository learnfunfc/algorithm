# bubble sorting

num = [3,1,7,12,10,5]
n = len(num)
i = 1 # 第一回合
while i<n-1:   
    for j in range(n-i): # n-i次比較
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1],num[j]
    i+=1

print(num)