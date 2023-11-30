def MyMultiple(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(MyMultiple(1,2,5))