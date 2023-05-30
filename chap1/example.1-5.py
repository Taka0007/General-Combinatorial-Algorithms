import math

# x^2 -bx - c=0 の解を求めるプログラム
# x_0は代数的な解、x_1は近似解
# その差を出力する

# 定数の代入
b = 777
c = 6787
#方程式を直接解いた時の解
x_0 = (math.sqrt(b**2+4*c)+b)/2

def f(x):
  return x**2-b*x-c


#近似解
error = 2**(-40)
left  = 0
right = 300
root_c   = (left+right)/2

while abs(left-right)>error:
    if root_c **2 - c<0:
        left = root_c
        root_c  = (left+right)/2
    else:
        right = root_c
        root_c  = (left+right)/2

x_1 = root_c + b/2

alfa = (x_1/x_0)
print(alfa)
print('x0:',x_0)
print('x1:',x_1)

print('f(x_0):',f(x_0))
print('f(x_1):',f(x_1))

print(math.sqrt(c))
print(root_c)