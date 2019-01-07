
"selection sorting"
num = [14,1,13,7,15]
i = 0 
while i < len(num)-1:
    j = i + 1
    while j < len(num):
        if num[i]> num[j]:
            num[i],num[j] = num[j],num[i]
        j+=1
    i+=1
print(num)