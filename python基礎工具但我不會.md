if 判斷式
------
基本語法一
if 布林值:
	若布林值為True,執行命令
基本語法二:
if 布林值:
	若布林值為True,執行命令
else:
	若布林值為False,執行命令
基本語法三:
if 布林值一:
	若布林值一為True,執行命令
elif 布林值二:
	若布林值二為True,執行命令
else:
	若布林值一和二都False,執行命令

程式範例
x=input("請輸入數字:")#基本輸入為字串型態
x=int(x)#轉換為整數型態
if x > 200:
	print("大於200")
elif

"""
類別基本語法:
------
定義(建立)類別
class 類別名稱:
    定義封裝的變數
    定義封裝的涵式

使用類別
類別名稱.屬性名稱

"""
#定義Test類別
class Test:
    x=3 #定義變數
    def say(): #定義函式
        print("Hello")
#使用Test類別
Test.x+3 #取得屬性x的資料 3
Test.say()#呼叫屬性say函式

=====================================
class Point:
    def __init__(self):
        self.x=3
        self.y=4
#建立實體物件
#此時體悟鑑包含x和y兩個實體屬性
p=Point()

#定義Test類別
class Test:
    x=3 #定義變數
    def say(): #定義函式
        print("Hello")
#使用Test類別
Test.x+3 #取得屬性x的資料 3
Test.say()#呼叫屬性say函式

#定義類別、與類別屬性(封裝在類別中的變數和函式)
#定義一個類別 IO, 有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrc=["console","file"]
    def read(src):
        if src not in IO.supportedSrc:
            print("Not supported")
        else:
            print("Read From", src)
#使用類別
print(IO.supportedSrc)
IO.read("file")
IO.read("Internet")

class Point:
    def __init__(self):
        self.x=3
        self.y=4
#建立實體物件
#此時體悟鑑包含x和y兩個實體屬性
p=Point()
