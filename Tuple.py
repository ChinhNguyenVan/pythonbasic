# 1, Tuple Trong Python là gì?
# Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ các đối tượng không thay đổi về sau (giống như hằng số).
#  Còn lại thì cách lưu trữ của nó cũng khá giống như kiểu dữ liệu list mà bài trước chúng ta đã được tìm hiểu.
# Để khai báo một enum thì mọi người sử dụng cú pháp sau:
# (val1, val2,.., valn)
# Trong đó, val1, val2,.., valn là các giá trị của tuple.

# VD: Mình sẽ khai báo 1 Tuple chứa các ngày trong tuần.

day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')

# Nếu bạn khai báo 1 biến chứa các giá trị mà không được bao quang bởi dấu () 
# thì Python cũng nhận định nó là một tuple.
# VD:

day = 'monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday'

# Và nếu như bạn muốn khai báo 1 tuple trống thì bạn chỉ cần khai báo như sau:

tupletrong = ();

# Còn nếu như tuple của bạn chỉ chứa duy nhất một giá trị thì bắt buộc bạn 
# phải thêm một dấu ',' nữa đằng sau giá trị đó.
# VD:

a = (10,)

# 2, Truy cập đến các phần tử trong Tuple.

day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
print(day)

# Truy cập theo kiểu từng phần tử
print(day[2])
print(day[-4])
# truy cập kiểu tupleName[start:end]
print(day[0:4])
print(day[-6:-3])

# 3, Tuple lồng.
day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday', day1)


print(day2)
