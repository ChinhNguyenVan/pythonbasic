# Các câu lệnh rẽ nhánh.
# if condition: 
#     #code
# else:
#     #code
# Example:
#========================================
a = 100
if (a == 100):
    print('Dung')
else:
    print('Sai')
#========================================
b = 5
if (b >= 0 and b <= 10):
    if (b >= 4):
        print('Qua mon')
    else:
        print('Hoc lai')
else:
    print('Diem khong hop le')

# Câu lệnh if-elif-else.
# if condition:
#     # code
# elif condition2:
#     # code
# elif condition3:
#     # code
# else:
#     #code

# VD: Mình sẽ giải quyết lại bài toán tính điểm ở trên bằng mệnh đề if-elif-else.

c = 9
if (c >= 4 and c <= 10):
    print('Qua mon')
elif (c >= 0 and c <4):
    print('Hoc lai')
else:
    print('Diem khong hop le')