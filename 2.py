#變數
a=b=c=10 #表示變數a,b,c皆指向int物件10
print(a,b,c)
a,b=5,15 #表示變數a指向物件5,變數b指向物件15
print(a,b,c)

#置換變數
x , y = 4,11
print("變數置換前",x,y)
x,y=y,x
print("變數置換後",x,y)
#eval字串運算式
print(eval('x+y'))
numA,numB,numC =eval(input('請輸入3個數值,以逗點隔開->'))
total =numA+numB+numC
print('合計',total)

#整數型別
_int = int(input('請輸入數值進行轉換'))
print('二進制:',bin(_int))
print('八進制:',oct(_int))
print('十六進制:',hex(_int))
Decimal=int(input('X進制='))
int_str=input('欲轉換的字串')
print(Decimal,'^2+',Decimal,'^1+',Decimal,'^0')
print(Decimal,'進制',int(int_str,Decimal))

#format
format_int = int(input('請輸入數值(format轉換)'))
print(format(format_int, 'b')) #二進制
print(format(format_int, 'o')) #十進制
print(format(format_int, 'x')) #十六進制
