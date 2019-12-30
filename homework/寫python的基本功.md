if 判斷式
------
基本語法一<br>
if 布林值:<br>
	若布林值為True,執行命令<br>
基本語法二:<br>
if 布林值:<br>
	若布林值為True,執行命令<br>
else:<br>
	若布林值為False,執行命令<br>
基本語法三:<br>
if 布林值一:<br>
	若布林值一為True,執行命令<br>
elif 布林值二:<br>
	若布林值二為True,執行命令<br>
else:<br>
	若布林值一和二都False,執行命令<br>

程式範例<br>
x=input("請輸入數字:")#基本輸入為字串型態<br>
x=int(x)#轉換為整數型態<br>
if x > 200:<br>
	print("大於200")<br>
elif<br>

"""
類別基本語法:
------
定義(建立)類別<br>
class 類別名稱:<br>
    定義封裝的變數<br>
    定義封裝的涵式<br>

使用類別<br>
類別名稱.屬性名稱<br>

"""
#定義Test類別<br>
class Test:<br>
    x=3 #定義變數<br>
    def say(): #定義函式<br>
        print("Hello")<br>
#使用Test類別<br>
Test.x+3 #取得屬性x的資料 3<br>
Test.say()#呼叫屬性say函式<br>

=====================================
class Point:<br>
    def __init__(self):<br>
        self.x=3<br>
        self.y=4<br>
#建立實體物件<br>
#此時體悟鑑包含x和y兩個實體屬性<br>
p=Point()<br>

#定義Test類別<br>
class Test:<br>
    x=3 #定義變數<br>
    def say(): #定義函式<br>
        print("Hello")<br>
#使用Test類別<br>
Test.x+3 #取得屬性x的資料 3<br>
Test.say()#呼叫屬性say函式<br>

#定義類別、與類別屬性(封裝在類別中的變數和函式)<br>
#定義一個類別 IO, 有兩個屬性 supportedSrcs 和 read<br>
class IO:<br>
    supportedSrc=["console","file"]<br>
    def read(src):<br>
        if src not in IO.supportedSrc:<br>
            print("Not supported")<br>
        else:<br>
            print("Read From", src)<br>
#使用類別<br>
print(IO.supportedSrc)<br>
IO.read("file")<br>
IO.read("Internet")<br>

class Point:<br>
    def __init__(self):<br>
        self.x=3<br>
        self.y=4<br>
#建立實體物件<br>
#此時體悟鑑包含x和y兩個實體屬性<br>
p=Point()<br>

