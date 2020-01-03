參考資料:
====
    http://puremonkey2010.blogspot.com/2013/05/alg-info-dijkstras-algorithm-shortest.html
    https://wkbjcloudbos.bdimg.com/v1/docconvert2842/wk/3bfeea509579331acfa80741eb26eeaf/0.png?responseContentType=image%2Fpng&responseCacheControl=max-age%3D3888000&responseExpires=Mon%2C%2017%20Feb%202020%2018%3A31%3A50%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2020-01-03T10%3A31%3A50Z%2F3600%2Fhost%2F48b619ed4f3858da82f6aec37feee5618db983add1563f199ab0a78ee30a2a7f&x-bce-range=0-9255&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3ODA1MTExMCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.SFux%2Bw9oe0RTl%2BbPukdEdC4lGl7dPHgUQcqUsf6gMF8%3D.1578051110)
    https://mropengate.blogspot.com/2015/01/algorithm-ch3-graph-algorithm.html
流程圖
------
![img](https://github.com/ghost36168/realreason/blob/master/%E5%9C%96%E7%89%87/%E6%BC%94%E7%AE%97%E6%B3%9501.jpg)

![img](https://github.com/ghost36168/realreason/blob/master/%E5%9C%96%E7%89%87/Kruskal's%20Algorithm.gif)
Dijkstra原理說明
------
        1.定義概覽

        Dijkstra(迪傑斯特拉)演算法是典型的單源最短路徑演算法，用於計算一個節點到其他所有節點的最短路徑。主要特點是以起始點為中心向外層層擴充套件，直到擴充套件到終點為止。Dijkstra演算法是很有代表性的最短路徑演算法，在很多專業課程中都作為基本內容有詳細的介紹，如資料結構，圖論，運籌學等等。注意該演算法要求圖中不存在負權邊。

        問題描述：在無向圖 G=(V,E) 中，假設每條邊 E[i] 的長度為 w[i]，找到由頂點 V0 到其餘各點的最短路徑。（單源最短路徑）

 

        2.演算法描述

        1)演算法思想：設G=(V,E)是一個帶權有向圖，把圖中頂點集合V分成兩組，第一組為已求出最短路徑的頂點集合（用S表示，初始時S中只有一個源點，以後每求得一條最短路徑 , 就將加入到集合S中，直到全部頂點都加入到S中，演算法就結束了），第二組為其餘未確定最短路徑的頂點集合（用U表示），按最短路徑長度的遞增次序依次把第二組的頂點加入S中。在加入的過程中，總保持從源點v到S中各頂點的最短路徑長度不大於從源點v到U中任何頂點的最短路徑長度。此外，每個頂點對應一個距離，S中的頂點的距離就是從v到此頂點的最短路徑長度，U中的頂點的距離，是從v到此頂點只包括S中的頂點為中間頂點的當前最短路徑長度。

        (1) 初始時，S只包含起點s；U包含除s外的其他頂點，且U中頂點的距離為”起點s到該頂點的距離”[例如，U中頂點v的距離為(s,v)的長度，然後s和v不相鄰，則v的距離為∞]。

        (2) 從U中選出”距離最短的頂點k”，並將頂點k加入到S中；同時，從U中移除頂點k。

        (3) 更新U中各個頂點到起點s的距離。之所以更新U中頂點的距離，是由於上一步中確定了k是求出最短路徑的頂點，從而可以利用k來更新其它頂點的距離；例如，(s,v)的距離可能大於(s,k) (k,v)的距離。

        (4) 重複步驟(2)和(3)，直到遍歷完所有頂點

Kruskal原理說明
------
    Kruskal是一種用來尋找最小生成樹的算法，在剩下的所有未選取的邊中，找最小邊，如果和已選取的邊構成回路，則放棄，選取次小邊。

    實現過程

    1).記Graph中有v個頂點，e個邊

    2).新建圖Graphnew，Graphnew中擁有原圖中相同的e個頂點，但沒有邊

    3).將原圖Graph中所有e個邊按權值從小到大排序

    4).循環：從權值最小的邊開始遍歷每條邊 直至圖Graph中所有的節點都在同一個連通分量中 if 這條邊連接的兩個節點於圖Graphnew中不在同一個連通分量中 添加這條邊到圖Graphnew中

