def backTracking(arr,curr,idx,size,rst):
    if size==idx:
        rst.append(curr.copy())
        return

    curr.append(arr[idx])
    backTracking(arr,curr,idx+1,size,rst)
    curr.pop()
    backTracking(arr,curr,idx+1,size,rst)

def perm(arr, idx, size, rst):
    if size == idx:
        rst.add((arr.copy()))
        return
    i = idx
    for i in range(idx, size):
        arr[i], arr[idx] = arr[idx], arr[i]
        perm(arr, idx + 1, size, rst)
        arr[idx], arr[i] = arr[i], arr[idx]

arrInput=[1,1,3]
rst=()
#backTracking(arrInput,[],0,len(arrInput),rst)
perm(arrInput,0,len(arrInput),rst)
print(rst)






