#  Cho một số a bất kỳ
print("Input a = ")
a = int(input())
# a. Trả về số lượng các bits cần thiết để biểu diễn số a ở dạng
# nhị phân, không bao gồm phần dấu và các số 0 ở đầu.

count = 0
if a < 0:
    a = -a
while a > 0:
    count += 1
    a = a >> 1
# b. Kiểm tra danh sách các thuộc tính và
# phương thức hiện tại của một biến có kiểu dữ liệu là number.

print(count)
list_Methods = dir(a)
for i in list_Methods :
    print(i)