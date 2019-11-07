程式碼是不能執行的
概念來源
------
    概念參考老師上課教材中的影片:https://www.youtube.com/watch?v=s8kQm8yhZ8U
    那我的程式
    arrA=[8,10,12,44,63]
    arrB=[2,3,20,106,144]
    arrC=[]
    i=0
    j=0
    right=arrA[i]
    left=arrB[j]
    while i<=len(arrA) or j<=len(arrB):
        if i<len(arrA) and j<len(arrB):
            if right<left:
                arrC.append(right)
                i=i+1
            else:
                arrC.append(left)
                j=j+1
        elif i<len(arrA) and j >=len(arrB):
            arrC[i+j+1:]=arrA[i+1:]
        else:
            arrC[i+j+1:]=arrB[j+1:]
        i=i+1
        j=j+1
    非常直觀，我將merge的流程一功能分為
    1.切割
    2.比大小和儲存
    3.重複執行
    我現在只有做步驟2，步驟1、步驟3沒做
    步驟2我覺得是核心的部分，但也沒做出來
    我的程式碼想的恨簡單，就跟老師影片上的一樣
    共有三個list，兩條已經切好的原來的list，一條空著準備進行交換的list
    如果左邊的值>右邊的值，那將左邊的值放進空著的值中
    因為左邊加右邊總儲放的值，就剛好等於雙方現在行經的值總和i+j
    那假如碰上奇數長度的list切割時，一邊長，一邊短，且還有值大小問題，導致一邊list所有值，都已存放進空著的資料夾了
    這是另一邊剩下的值要全放進空著的值不用排序，所以希望用[:]
    
    
