def bisearch(arr, target):
    low = 0
    high = len(arr) - 1
    while(low<=high):
        mid = int((low+high)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def bi_left(arr, target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = int((low+high)/2)
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        elif mid==0 or arr[mid-1]!=target:
            return mid
        else:
            high = mid -1
    return -1


def bi_right(arr, target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = int((low+high)/2)
        if arr[mid]>target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            if mid == len(arr)-1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                low = mid + 1
    return -1


def bi_small(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low+high)/2)
        if arr[mid] > target:
            high = mid - 1
        else:
            if mid==len(arr)-1 or arr[mid+1]>target:
                return mid
            else:
                low = mid + 1
    return -1


def bi_big(arr, target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = int((low+high)/2)
        if arr[mid] < target:
            low = mid + 1
        else:
            if mid==0 or arr[mid-1]<target:
                return mid
            else:
                high = mid -1
    return -1

arr = [1, 1, 1, 2, 3, 4, 5, 5, 5, 7, 11]
print(bisearch(arr, 2))
print(bi_left(arr, 2))
print(bi_right(arr, 2))
print(bi_small(arr, 12))
print(bi_big(arr, 11))
