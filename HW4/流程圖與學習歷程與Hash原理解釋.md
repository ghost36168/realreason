參考資料
------
    網址1:"https://ithelp.ithome.com.tw/articles/10208884"
    網址2:"https://blockbar.io/blockchain/hash%E6%98%AF%E4%BB%80%E9%BA%BC-what-is-hash/"
    網址3:"https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view"
    網址4:"http://www.tsnien.idv.tw/Security_WebBook/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E9%9B%9C%E6%B9%8A%E8%88%87%E4%BA%82%E6%95%B8%E6%BC%94%E7%AE%97%E6%B3%95.html"
    網址5:"https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8"
 Hash
 ------
        名詞定義:
        Hash是什麼？
        雜湊(Hash)算法原先是一種用在資料編碼中的技術，最主要分為Hash Function（雜湊函數）和Hash Table（雜湊表）兩個部份，
        其中hash function是一種將任         意資料映射成為固定長度的技術，hash table則是儲存（Key,Value）這種對應關係的資料結構
        Hash Function是什麼？
        雜湊函式Hash Function是一種將輸入值映射到另一個值域的技術，Hash Function的底層有非常複雜的數學式，
        式子中蘊含了一些magic number，有興趣鑽研的  可以再去尋找一些論文來研讀，
        這邊就不多作介紹，因此在這邊可以直接想像Hash Function就是一台轉換器，丟輸入進去就會產生一個輸出，
        而這種轉換有一個很重要的特性就是「單向」，也就是one-way function，
        輸入可以經由轉換得到輸出，但輸出卻不可得到輸入，具有不可逆的特性。
        Hash Table是什麼？
        雜湊表是雜湊函式的一個主要應用，使用雜湊表能夠快速的按照關鍵字尋找資料記錄。
        注意：關鍵字不是像在加密中所使用的那樣是秘密的，但它們都是用來「解鎖」或者存取資料的。）
        簡單說
        雜湊表Hash Table是一種儲存（Key,Value）的資料結構，通常一個Key就是對應一個Value，Value就是要儲存的資料，
        Key則可以想像成這筆資料的標籤，想要找到這筆資料就需要有這筆資料的Key去搜尋
        應用流程:
        第一階段 Array
        (Key)                 (hash value)     (stored index)
    Joe  → (Hash function) →   4928   mod 5   =   3
    Sue  → (Hash function) →   7291   mod 5   =   1
    Dan  → (Hash function) →   1539   mod 5   =   4
    Nell → (Hash function) →   6276   mod 5   =   1
    Ally → (Hash function) →   9143   mod 5   =   3
    Bob  → (Hash function) →   5278   mod 5   =   3
        第二階段 Linked List:(下方的圖片)
   ![image](https://github.com/ghost36168/realreason/blob/master/%E5%9C%96%E7%89%87/%E9%A1%9E%E4%BC%BC%E8%80%81%E5%B8%AB%E7%9A%84%E6%B5%81%E7%A8%8B%E5%9C%96%E4%BD%86%E6%98%AF%E6%88%91%E5%9C%A8%E7%B6%B2%E8%B7%AF%E4%B8%8A%E6%89%BE%E7%9A%84.png)
        
流程圖
------
![image](https://github.com/ghost36168/realreason/blob/master/%E5%9C%96%E7%89%87/HW4(%E6%89%8B%E7%B9%AA)%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)

學習歷程
------
       技術債，就是債，要記的還，否則很慘!!!!!!!
       如果不談Linked List欠債問題，這次重心理當在如何銜接，兩種截然不同的資料結構
       之所以這麼想是因為，老師這次講得太清楚了，清楚到就幾乎只剩技術問題，不存在觀念上、理念上歧異的問題。
       我目前的技術問題卡在為甚麼
       老師的程式碼中
       class MyHashSet:
    def __init__(self,capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    def add(self,key: int) ->None:
        idx =key% self.capacity
        node =self.data[idx]
        while node:
            if node.val == key:
                return
            node = node.next
        new_node = ListNode(key)
        new_node.next = self.data[idx]
        self.data[idx] = new_node
        ...
        node.val 從甚麼地方跑出來的，百思不得其解，就開始亂想
        self.xxx
        xxx 可以亂填
        但它是node不是self
        難道 self.val 完全等同 node.val ???
        完全想不通
        唉!我再想想吧!!
        
