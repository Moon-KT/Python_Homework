def sum(array, t):
    sum = 0
    for i in range(t):
        sum += array[i]
    return sum

def array():
    n = int(input("Enter number n: "))
    a = []
    for i in range(n):
        m = int(input("Enter a[" + str(i) + "]: "))
        a.append(m)

    t = int(input("Enter number t: "))
    for i in range(t):
        m = int(input("Enter t[" + str(i) + "]: "))
        print( "Sum: " + str(sum(a, m)))

array()
