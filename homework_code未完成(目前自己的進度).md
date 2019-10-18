alist=[2,5,8,9,7,6,5,9,8,2,5]
right=[]
i=0
while i<len(alist):
    if alist[i]>alist[-1]:
        right.append(alist[i])
    else:
        print("little")
    i=i+1
    
   =====================
alist=[2,5,8,9,7,6,5,9,8,2,5]
right=[]
left=[]
i=0
while i<len(alist):
    if alist[i]>alist[-1]:
        right.append(alist[i])
    else:
        left.append(alist[i])
    i=i+1
