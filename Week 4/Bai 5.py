# trai phang list
def final_list(my_list):
    res = []
    for i in my_list:
        if isinstance(i,list):# kiem tra la list hay ko ?
            res.extend(final_list(i))
        else:
            res.append(i)
    return res

my_list = [0, 10, [20, 30], 40, 50, [60, 70, [70, 80], 80], [90, 100, 110, 120]]

res = final_list(my_list)
print(res)

