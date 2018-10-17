def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        flag = False  # 交换标志，如果没有交换了，说明数据已经有序，不再需要循环了，减少了不必要的比较
        for j in range(n-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                flag = True
        if flag == False:
            return alist
    return

def insert_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]   # 前部分为有序部分，如果alist[j]不小于alist[j-1]
            else:                                             # 那么alist[j]就一定也不会小于alist[j-1]之前的数
                break                                         # 所以小循环也就可以被break了
    return

def select_sort(alist):
    n = len(alist)
    for i in range(n):
        min_val = alist[i]
        index = i
        for j in range(i+1, n):
            if alist[j]<min_val:
                min_val = alist[j]
                index = j
        alist[i], alist[index] = alist[index], alist[i]
    return

alist = [1,2,6,3,2,5,4,4,1]
insert_sort(alist)
print(alist)





