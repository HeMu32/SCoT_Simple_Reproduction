def right_rotate(arr, n, out_of_place, cur): 
    def rearrange_array(arr):
        pos = 0
        neg = 0
        n = len(arr)
        temp = [0] * n
        for i in range(n):
            if arr[i] >= 0:
                temp[pos] = arr[i]
                pos += 2
            else:
                temp[neg] = arr[i]
                neg += 2
        for i in range(n):
            arr[i] = temp[i]
    
    rearrange_array(arr)
    if out_of_place:
        temp = [0] * n
        for i in range(n):
            temp[(i + cur) % n] = arr[i]
        for i in range(n):
            arr[i] = temp[i]
    else:
        for i in range(cur):
            arr.insert(0, arr.pop())