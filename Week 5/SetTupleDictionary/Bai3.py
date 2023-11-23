import re

my_str = input()

cat_xau = re.split(r'\W+', my_str)

tan_suat = {}
for word in cat_xau:
    if len(word) != 0:
        if word in tan_suat:
            tan_suat[word] += 1
        else:
            tan_suat[word] = 1

nhieu_nhat = max(tan_suat.values())

ket_qua = {word: freq for word, freq in tan_suat.items() if freq == nhieu_nhat}

my_tuple = tuple(ket_qua.items())
print(my_tuple)
