my_str = input()
my_dict = {}
for s in my_str:
    if s in my_dict:
        my_dict[s] += 1
    else:
        my_dict[s] = 1
print(my_dict)
