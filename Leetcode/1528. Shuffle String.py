def restoreString(s, indices):
    R = len(s)
    i=0
    arr = []
    brr = []
    for j in s:
        arr.append(j)
        brr.append(j)
    for k in indices:
        brr[k]=arr[i]
        i+=1
    return brr
s = "aiohn"
indices = [3,1,4,2,0]
print(restoreString(s, indices))

# arr[0]=brr[4]   l
# arr[1] brr[5]   e
# arr[2] brr[6]   e
# arr[3] brr[7]   t
# arr[4] brr[0]   c
# arr[5] brr[2]   d
# arr[6] brr[1]   o
# arr[7] brr[3]   e