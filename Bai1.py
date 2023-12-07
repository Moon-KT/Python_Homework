class Pycon:
    id = 0
    total_age = 0
    total_pycons = 0

    def __init__(self, name, age):
        Pycon.id += 1
        self.id = Pycon.id
        self.name = name
        self.age = age
        Pycon.total_age += age
        Pycon.total_pycons += 1

    @classmethod
    def average_age(cls):
        return cls.total_age / cls.total_pycons

    def __str__(self):
        return f'Id: {self.id} || Tên: {self.name} || Tuổi: {self.age}'

    @staticmethod
    def nhap():
        name = input("Nhập tên Pycon: ")
        age = int(input("Nhập tuổi Pycon: "))
        return Pycon(name, age)


# Nhập thông tin Pycon
n = int(input("Nhập số lượng Pycon: "))
pycons = []
for i in range(n):
    pycon = Pycon.nhap()
    pycons.append(pycon)

# In thông tin Pycon
for pycon in pycons:
    print(pycon)

# Tính trung bình tuổi Pycon
print(f'Trung bình tuổi: {Pycon.average_age()}')
