作業程式碼(圖片)+解釋+成果展示
====
首先要先澄清，這程式碼是我從網路上找來，所以這不是我寫的，我寫的在隔壁棚。我是以它為藍底，我的沒寫完。但我想我的程式寫完，會極度相像。我挑這篇，原因是這是我目前看到別人寫，最淺顯易懂，最簡潔的一位，與我最初構想相近的，可說是我好幾倍的加強版
------
![image](別人的程式碼.PNG)

解釋
------

    def quick_sort(list):  
        smaller = []   
        bigger = []   
        keylist = []   

        if len(list) <= 1:
            return list

        else:
            key = list[-1] #最後一個數為key值
            for i in list:
                if i < key: #比key值小的數
                    smaller.append(i)
                elif i > key: #比key值大的數
                    bigger.append(i)
                else:
                    keylist.append(i)

        smaller = quick_sort(smaller)
        bigger = quick_sort(bigger)
        return smaller + keylist + bigger
    當中核心觀念:在quick_sort 的排序是通過比大小而來的。  
    恰好quicksort本身的演算法就是重複與list的最後一值比較，進而切分成區段
    跟最後一值比較，只有三種情況，要嘛大於、小於、等於
    基於上述觀念:
    所以才分三類 
    剛開始這三類先讓它空著，等比大小再裝進去，保持靈活調度空間 
    然後就與key(最後一值)比大小，裝近三個袋子中 
    倒數第三行與第二行，應該是通篇程式碼最難處
    採取遞迴的方式，將已經拆分出去的smaller,bigger，這兩團其實仍未排好順序，大小錯置的情形存在，
    遂再丟進def加以分類
    最終將其集合
成果展示
====
![image](其學習成果展現.PNG)
