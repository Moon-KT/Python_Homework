# Chia nho theo n

my_list = list(map(int, input("Enter list: ").split()))

n = int(input("Enter n: "))

huhu = []
if len(my_list) % n != 0:
    print("Not a divisor of ", len(my_list))
else:
    for i in range(n):
        new_list = []
        for j in range(i, len(my_list), n):
            new_list.append(my_list[j])
        huhu.append(new_list)
    print("Ater list:  hehe = ", huhu)