# dem tu ngay do den cuoi anwm cos bao nhieu ngay

s = input("Enter string: ")

list = s.split('/')
count = 0
try:
    dd = int(list[0])
    mm = int(list[1])
    yyyy = int(list[2])

    # Kiem tra khoang
    l =  ((True if yyyy >= 1000 else False ) if 1 <= mm <= 12 else False ) if 1 <= dd <= 31 else False

    # Kiem tra nam nhuan
    k =  True if ( mm == 2 and dd <= 28 ) else False

    # Kiem tra thang 2
    if ( yyyy % 4 == 0 and yyyy % 100 != 0):
        # month_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        count = ( 2 if l == True else count ) if k == True else 1
        print(count)
        count += month_day[mm - 1] - dd + sum(month_day[i] for i in range(mm, 12))
        print("Countdown to New Year " , count)
    else: print('Invalid')

except:
    print('Invalid')
