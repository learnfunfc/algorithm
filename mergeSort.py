s = [26, 5, 7, 1, 41, 11, 9, 15, 48, 19]

def merge2(low, mid, high):
    global s
    left_list = s[low:mid+1] # 切割左右半部
    right_list = s[mid+1:high+1]
    #print(left_list,right_list)
    i = 0
    j = 0
    k = low
    while (i < len(left_list) and j < len(right_list)):
        if left_list[i] <= right_list[j]:  # 左數字<= 右數字
            s[k] = left_list[i]  # s清單放入左邊數字
            i += 1
        else:
            s[k] = right_list[j]  # s清單放入右邊數字
            j += 1
        k += 1

    
    if (i > len(left_list)):  # 如果i先走完，則把剩餘右半邊填入s清單
        while j < len(right_list): #注意小於符號 不是小於等於
            s[k] = right_list[j] 
            k += 1
            j += 1
    else:
        while i < len(left_list):  # 如果j先走完，把剩餘左半邊填入s清單
            s[k] = left_list[i]
            k += 1
            i += 1


def mergeSort2(low, high):
    # 主程式切割
    if (low < high):
        mid = (low+high)//2
        mergeSort2(low, mid)  # 左半邊切割
        mergeSort2(mid+1, high)  # 右半邊切割

        merge2(low, mid, high)  # 合併


mergeSort2(0, 9)
print(s)
