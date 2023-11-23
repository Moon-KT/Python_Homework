#Chia thanh cac tahnh phan giong nhau thanh list con

my_list = list(map( int, input("Enter list: ").split()))
my_list.sort()

new_list = []
hihi = []

for i in my_list:
    if len(new_list) == 0 or i in new_list:
        new_list.append(i)
    elif not i in new_list:
        hihi.append(list(new_list))
        new_list.clear()
        new_list.append(i)

if new_list:
    hihi.append(list(new_list))

print("After list:", hihi)
