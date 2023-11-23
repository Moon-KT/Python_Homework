# tong chan vs le

n = int(input("Enter amount: "))

a = [0]*n
for i in range(n):
    a[i] = int(input("Enter a[" + str(i + 1)+ "] = " ))

compare = sum( i for i in range(n) if a[i] % 2 == 0 ) - sum( i for i in range(n) if a[i] % 2 != 0 )

if compare > 0:
    print("even")
elif compare < 0:
    print("odd")
else: print("equal")
