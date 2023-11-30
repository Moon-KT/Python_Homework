x = list(map(int, input().split()))
y = list(map(int, input().split()))
c = []
Tong = 0
w, b = float(input()),float(input())
for i in range(len(x)):
    Gia_uoc_tinh = x[i]*w +b
    c.append(Gia_uoc_tinh)

for i in range(len(x)):
    Tong += (c[i] - y[i])**2

Loss = 1// ( 2*len(x))*Tong

