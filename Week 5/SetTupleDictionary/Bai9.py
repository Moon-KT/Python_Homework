import random as r

n = 0
while True:
    try:
        n = int(input("Nhập số lượng sinh viên: "))
        if n < 10 or n > 99999:
            print("Số lượng trong vòng [10, 99999]!")
            continue
        break
    except ValueError:
        print("Số lượng trong vòng [10, 99999]!")

ds_mat_khau = ["CNTT", "KHMT", "KTPM", "HTTT"]
ds_tksv = {}
for i in range(n):
    tai_khoan = input("Nhập tài khoản: ")
    mat_khau = r.choice(ds_mat_khau)
    print("Mật khẩu của bạn là: " + mat_khau)
    ds_tksv[tai_khoan] = mat_khau

print(ds_tksv)
