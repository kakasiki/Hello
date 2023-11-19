print(round(2.1345,3))
x=complex(2,3)
print(x)
print(type(eval('500/10')))
from math import sqrt
print( sqrt(4)*sqrt(4) == 4 )
x=(1,)
print(type(x))
ls = []
Dcountry = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
print(Dcountry.get('美国', '悉尼'))
print(Dcountry.get('澳大利亚', '悉尼'))
try:
    alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx=eval(input("请输入一个整数"))
    print(alp[idx])
except NameError:
    print("print 1")
else:
    print("print 2")   #不执行except就会顺序执行
finally:
    print("print 3")
x=1,2,3
print(type(x))
#get("key","value"),若字典中无key则返回value
#s={}为空字典，s=set()空集合，s=[]空列表，s=list[]空列表