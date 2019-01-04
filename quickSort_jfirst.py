''' 請注意此版本是j先走再換i走'''
def Qsort(num,m,n):   
    if m<n: # 如果元素大於一個以上 執行繼續遞迴分群
        i = m # 設i等於起始索引值
        j = n # 設j等於終止索引值
        k = num[m] #設 pivot key等於 第一個數值
        
        while i!=j:        
            while (num[j]>=k and i<j): #j 先往左走 找到比k小停下
                j = j - 1
            while (num[i]<=k and i<j): #i 再往右走 找到比k大停下
                i = i + 1
            if (i<j): # 只有i<j時才能交換，才不會i,j交錯時產生互換的情形
                num[i],num[j] = num[j],num[i]
            
        num[m], num[j] = num[j] ,num[m] # 當i>=j時， j上的值和k值互換
        Qsort(num,m,j-1) # 左半邊遞迴
        Qsort(num,j+1,n) # 右半邊遞迴

num=[11,2,151,41,5,12,9]
Qsort(num,0,len(num)-1)
print(num)
