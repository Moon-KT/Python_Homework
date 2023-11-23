mssv = list(map(str, input().split()))
dtk = list(map(float, input().split()))

my_dict = {mssv[i]: dtk[i] for i in range(0, len(mssv))}
print(my_dict)

diem_trong_doan = {mssv[i]: dtk[i] for i in range(0, len(mssv)) if 2.5 <= dtk[i] <= 3.5}
print(diem_trong_doan)

mssv.append(input())
dtk.append(float(input()))
sau_khi_them = {mssv[i]: dtk[i] for i in range(0, len(mssv))}
print(sau_khi_them)

for i in range(len(mssv) - 1, -1, -1):
    if dtk[i] < 2:
        mssv.remove(mssv[i])
        dtk.remove(dtk[i])
sau_khi_xoa = {mssv[i]: dtk[i] for i in range(0, len(mssv))}
print(sau_khi_xoa)
