class Hiter:
    def __init__(self, id, ten, tuoi, gen):
        self.id = id
        self.ten = ten
        self.tuoi = tuoi
        self.gen = gen

    @staticmethod
    def nhap():
        id = int(input("Nhập ID: "))
        ten = input("Nhập tên: ")
        tuoi = int(input("Nhập tuổi: "))
        gen = input("Nhập giới tính: ")
        return Hiter(id, ten, tuoi, gen)

    def __str__(self):
        return f'Id: {self.id}, ten: {self.ten}, tuoi: {self.tuoi}, gen: {self.gen}'


class Ban:
    def __init__(self, idban, tenban, truongban: Hiter, *thanhvien: Hiter):
        self.idban = idban
        self.tenban = tenban
        self.truongban = truongban
        self.thanhvien = list(thanhvien)

    @staticmethod
    def nhap():
        idban = int(input("Nhập ID Ban: "))
        tenban = input("Nhập tên Ban: ")
        truongban = Hiter.nhap()
        return Ban(idban, tenban, truongban)

    def __str__(self):
        return f'Ban: id: {self.idban}, ten: {self.tenban}, truong ban: {self.truongban}'

    def xoa(self, ten_hiter):
        for hiter in self.thanhvien:
            if hiter.ten == ten_hiter:
                self.thanhvien.remove(hiter)
                break

    def add(self, hiter):
        self.thanhvien.append(hiter)


# Nhập n Hiter và in ra thông tin n hiter đó
n = int(input("Nhập số lượng Hiter: "))
hiters = []

for i in range(n):
    h = Hiter.nhap()
    hiters.append(h)

print("Danh sách Hiter:")
for h in hiters:
    print(h)

# Nhập m Ban và in ra thông tin m ban đó
m = int(input("Nhập số lượng Ban: "))
bans = []

for i in range(m):
    b = Ban.nhap()
    bans.append(b)

print("Danh sách Ban:")
for b in bans:
    print(b)

# Nhập tên ban và xóa 1 hiter ban đó
ten_ban = input("Nhập tên Ban cần xóa Hiter: ")
ten_hiter = input("Nhập tên Hiter cần xóa: ")

for ban in bans:
    if ban.tenban == ten_ban:
        ban.xoa(ten_hiter)
        break

# Thêm một Hiter vào ban
new_hiter = Hiter.nhap()

for ban in bans:
    ban.add(new_hiter)

print("Danh sách Ban sau khi xóa và thêm Hiter mới:")
for b in bans:
    print(b)
