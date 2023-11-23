my_list = set(map(int, input().split()))

if 11 not in my_list:
    my_list.add(11)
print(my_list)

result = []
temp = list(map(int, my_list))
for i in temp:
    diff = 11 - i
    if diff in temp and diff != i:
        result.append((diff, i))
final_result = tuple(result)
print(final_result)
