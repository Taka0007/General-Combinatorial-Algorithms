# 3x^2-2x-4の解を2^(-k)の精度で求める

def f(x):
    return 3*(x**2)-2*x-4

k = int(input())
error = 2**(-k)

left  = -(10**3)
right = (10**3)
mid   = (left+right)/2

while abs(f(mid))>error:
    if f(mid)>0:
        right = mid
        mid   = (left+right)/2
        
    else:
        left = mid
        mid  = (left+right)/2
        
print(mid)
