# List tang dan cua cac so yeu thik( 1, 3, 5, 7, 9) trong day

while True:
    n = int(input("Enter length: "))
    if n < 1 and n > 100:
        print("Re-enter: ")
    else: break

res = []

for i in range(n):
    num = int(input("Enter element " + str(i + 1) + ": "))
    if (num % 10) % 2 == 1:
        res.append(num)

res.sort()
print(len(res))

for i in res:
    print(i, end = " ")