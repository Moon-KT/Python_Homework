# De o homework : chs tro chs

# Giá trị cần trong trò chơi
loi_A = 0           # Lỗi qua các round của người chs 1
loi_B = 0           # Lỗi qua các round của người chs 2
tong_win_A = 0      # Tổng lần thắng của người chs 1
tong_win_B = 0      # Tổng lần thắng của người chs 2
dem_round = 0       # đếm số round đã chơi
list_win_A = []     # Danh sách thắng của người chs 1
list_win_B = []     # Danh sách thắng của người chs 2

#Thực hiện trò chơi
while True:
    #Lựa chọn nên nghiện hay không?
    print("\nBạn có muốn chơi game không?\n\tĐồng ý : Y và Từ chối: N ")
    lua_chon = input("Nhập lựa chọn: ")
    if lua_chon == "N":
        break
    elif lua_chon == "Y":

        # Bắt đầu nghiện
        print("\nQuy định trước khi chơi:")
        print("\t1.Người chơi thứ nhất là A\n\t  Người chơi thứ hai là B")
        print("\t2.Tổng số diêm /n/ phải là 1 số nguyên dương")
        print("\t3.Số diêm được nhặt mỗi lượt /k/ phải là một số nguyên dương và không vượt quá số diêm hiện có!")

        # Vận hành các thông số
        while True:
            print("\nNhập thông số trò chơi: ")
            try:
                tong_diem_n = int(input("Nhập số lượng diêm mở màn n = "))
                if tong_diem_n < 1:
                    print("\nNhập lại: ")
                else:
                    break
            except:
                print("Lỗi, dữ liệu bạn vừa nhập không phải số")

        while True:
            try:
                boc_diem_k = int(input("Nhập số diêm bốc tối đa k = "))
                if boc_diem_k < 1 or boc_diem_k > tong_diem_n:
                    print("\nNhập lại: ")
                else:
                    break
            except:
                print("Lỗi, dữ liệu bạn vừa nhập không phải số")
        dem_round += 1

        # Bắt đầu trò chơi
        luot_boc = 0
        print("-----Start-----")
        while tong_diem_n > 0:
            if luot_boc % 2 == 0:
                print("\nLượt của người chơi thứ nhất: ")
            else:
                print("\nLượt của người chơi thứ hai: ")
            luot_boc += 1
            try:
                diem_boc_hien_tai = int(input("\tNhập số que diem được bốc trong lượt : "))
                if diem_boc_hien_tai < 1 and diem_boc_hien_tai > boc_diem_k and diem_boc_hien_tai > tong_diem_n:
                    print("Nhập lại: ")

                    if luot_boc % 2 == 0:
                        loi_A += 1
                    else:
                        loi_B += 1
            except:
                print("Lỗi, dữ liệu bạn vừa nhập không phải số")

            tong_diem_n -= diem_boc_hien_tai

            if tong_diem_n == 0:
                print("-----End----")
                if luot_boc % 2 == 0:
                    print("Người chơi A đã thua cuộc")
                    tong_win_B += 1
                    list_win_A.append(dem_round)
                else:
                    print("Người chơi B đã thua cuộc")
                    tong_win_A += 1
                    list_win_B.append(dem_round)

    else:
        print("Chọn lại đê:")

# Kết quả chung cuộc
print("-----Thống kê kết quả sau", dem_round ,"vòng chơi:----- ")

print("Kết quả chung cuộc: ", end = "")
if len(list_win_A) > len(list_win_B):
    print(" người chơi A đã thắng!\nCác vòng người chơi A thắng: ", list_win_A)
elif len(list_win_A) < len(list_win_B):
    print(" người chơi B đã thắng!\nCác vòng người chơi B thắng: ", list_win_B)
elif loi_A > loi_B:
    print("Người chơi A đã thắng!\nCác vòng người chơi A thắng: ", list_win_A)
elif loi_A < loi_B:
    print("Người chơi B đã thắng!\nCác vòng người chơi B thắng: ", list_win_B)
else:
    print("Hoà chung cuộc")



