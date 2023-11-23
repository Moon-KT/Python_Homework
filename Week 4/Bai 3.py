# tong so trong xau
import re

str = input("Enter string: ")

list = re.findall(r'-?\d+', str)

sum = sum(int(i) for i in list )
print("Sum of list: ", sum)


# Note trên slide Buổi 4:
# findall(pattern, str): return 1 list chứa tất cả các matches
#  \ special charecter  Vd re.findall(“\d”, txt)
#  ? xuất hiện 0 hoặc 1 Vdre.findall(“.?t”, txt)

