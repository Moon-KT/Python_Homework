
print("Nhap a = " )
a = int(input())

print("Nhap b = ")
b = int(input())

print( "a.", a ,"+", b ," = ", a + b )
print( "b.", a ,"-", b ," = ", a - b )
print( "c.", a ,"*", b ," = ", a*b )
print( "d.", a ,"/", b ," = ", a/b )
print( "e.", a ,"**", b ," = ", a**b  )
print( "f.", a ,"%", b ," = ", a%b )

print( "g. Compare a = ", a ," with b = ", b ," :", "a == b" if a == b else "a > b" if a > b else " a < b ")

print( "h.", a ,"AND", b ," = ", a and b  )
print( "i.", a ,"OR", b ," = ", a or b  )
print( "j.", a ,"XOR", b ," = ", not (a or b)  )
print( "k. NOT", a ,"==", b ," = ", not a == b  )
print( "l.", a ,"dịch phải 5 bit:", a>>5 )
print( "m.", a ,"dịch trái 6 bit", a << 6 )

print("n. ", bin(a) [2:][::-1])