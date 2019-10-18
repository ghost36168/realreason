
alist=[2,5,8,9,7,6,5,9,8,2,5]
right=[]
while i<len(alist):
    if alist[i]>alist[-1]:
        right.append(alist[i])
    else:
        print("little")
    i=i+1
