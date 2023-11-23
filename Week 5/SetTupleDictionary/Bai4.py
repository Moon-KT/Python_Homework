import re

n = int(input())

my_list = []

for i in range(n):
    my_list.append(input())

my_tuple = tuple(my_list)
print(my_tuple)

result_list = []
for s in my_list:
    if re.search(r"\d+", s):
        result_list.append(s)
print(len(result_list))
