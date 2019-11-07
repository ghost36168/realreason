條件限制:奇數&正整數
s=len(alist)
k=int((s-2)/2)
while s<=len(alist) and s>= 2:
    if alist[2*k+1] > alist[k] and alist[2*k+2]>alist[k]:
        if alist[2*k+1] > alist[2*k+2]:
            temp=[]
            temp=alist[k]
            alist[k]=alist[2*k+1]
            alist[2*k+1]=temp
        else :
            temp=[]
            temp=alist[k]
            alist[k]=alist[2*k+2]
            alist[2*k+2]=temp
    elif alist[2*k+1] > alist[k] and alist[2*k+2] < alist[k]:
        temp=[]
        temp=alist[k]
        alist[k]=alist[2*k+1]
        alist[2*k+1]=temp
    elif alist[2*k+2] > alist[k] and alist[2*k+1] < alist[k]:
        temp=[]
        temp=alist[k]
        alist[k]=alist[2*k+2]
        alist[2*k+2]=temp
    else:
        alist[k]=alist[k]
        alist[2*k+1]=alist[2*k+1]
        alist[2*k+2]=alist[2*k+2]
s=s-1
