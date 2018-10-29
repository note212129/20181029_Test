#我是單行註解
"""   我
      是
      多
      行
      註
      解"""

#簡單程式範例
""" print表示輸出結果
    input表示取得輸入值"""

print("Welcome Python領域")
age = int(input("請輸入您的年齡"))
if age >=20:#進行條件判斷
      print("您有投票權")
else:
      print("未滿"+str(age)+"沒有投票權")

#多行合併:使用半形分號「;」將多行合併
a=10;b=20;c=30

#分行:末端使用倒斜線「\」將一行折成兩行
print(a*10000+b*1000\
          +c*100)
#print
print(16,15,sep="&",end='')
print(99,37)
