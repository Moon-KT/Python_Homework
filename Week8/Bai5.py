from math import gcd


class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    @staticmethod
    def from_hon_so(hon_so):
        tu_so = hon_so.phan_nguyen * hon_so.phan_phan_so.mau_so + hon_so.phan_phan_so.tu_so
        mau_so = hon_so.phan_phan_so.mau_so
        return PhanSo(tu_so, mau_so)

    def __str__(self):
        return f'Tu_so: {self.tu_so} ,mau_so: {self.mau_so}'


class HonSo:
    def __init__(self, phan_nguyen, phan_phan_so):
        self.phan_nguyen = phan_nguyen
        self.phan_phan_so = phan_phan_so

    @staticmethod
    def from_phan_so(phan_so):
        phan_nguyen = phan_so.tu_so // phan_so.mau_so
        tu_so = phan_so.tu_so % phan_so.mau_so
        mau_so = phan_so.mau_so
        return HonSo(phan_nguyen, PhanSo(tu_so, mau_so))

    def __str__(self):
        return f'Phan_nguyen: {self.phan_nguyen} ,phan phan so: {self.phan_phan_so}'


class Math:
    def __init__(self, a):
        self.a = a

    def cong(self, other):
        tu_so = self.a.tu_so * other.a.mau_so + other.a.tu_so * self.a.mau_so
        mau_so = self.a.mau_so * other.a.mau_so
        ucln = gcd(tu_so, mau_so)
        return PhanSo(tu_so // ucln, mau_so // ucln)

    def nhan(self, other):
        tu_so = self.a.tu_so * other.a.tu_so
        mau_so = self.a.mau_so * other.a.mau_so
        ucln = gcd(tu_so, mau_so)
        return PhanSo(tu_so // ucln, mau_so // ucln)


# Nhập 2 đối tượng Math, 1 dạng phân số, 1 dạng hỗn số
a = Math(PhanSo(1, 2))
b = Math(HonSo(1, PhanSo(1, 2)))

# Đổi a thành hỗn số, b thành phân số và in lại a, b lên màn hình
a = HonSo.from_phan_so(a)
b = PhanSo.from_hon_so(b)
print("a:", a)
print("b:", b)

# In ra kết quả của a+b, b+a, a*b và b*a
print("a + b:", a.cong(b))
print("b + a:", b.cong(a))
print("a * b:", a.nhan(b))
print("b * a:", b.nhan(a))
