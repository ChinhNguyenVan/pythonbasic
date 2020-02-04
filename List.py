# 1, List là gì? và khai báo list trong Python.
# List trong Python là một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau trong nó, 
# và chũng ta có thể truy xuất đến các phần tử bên trong nó thông qua vị trí của phần tử đó trong list. 
# Ở đây, nếu như bạn nào đã tìm hiểu qua một ngôn ngữ nào đó thì có thể coi list trong Python 
# như một mảng tuần tự trong các ngôn ngữ khác.

# Để khai báo một list trong Python thì chúng ta sử dụng cặp dấu [] và bên trong là các giá trị của list.
# [value1, value2,..., valueN]
# Trong đó: value1, value2,..., valueN là các giá trị của list.

# VD: Mình sẽ khai báo 1 list chứa tên các học sinh.

name = ['NGUYEN VAN CHINH', 'VO VAN LINH', 'NGUYEN VAN TU','NGUYEN XUAN HAO']


# 2, Truy cập đến các giá trị trong list.
name = ['NGUYEN VAN CHINH', 'VO VAN LINH', 'NGUYEN VAN TU','NGUYEN XUAN HAO']

print(name[-1])
print(name[-2])
print(name[0])
print(name[1])

#list[start:end]
print(name[0:1])
print(name[0:2])
print(name[-4:-1])

# 3, Sửa đổi và xóa bỏ giá trị phần tử trong list.

name1 = ['MAI NANG LEN', 'LUNG THI LINH', 'NONG MANH ONG','VU THI LAN']

#Update
name1[2] = 'HOANG THUY LINH'
print(name1)

#Delete
del name1[1]
print(name1)

# 4, List lồng nhau.
#Do list có thể chứa nhiều kiểu dữ liệu khác nhau lên 
# chúng ta hoàn toàn có thể khai báo một list chứa một hoặc nhiều list khác nhau.

FullName=[name,name1]
print(FullName)

name2=[1,'hello','loto',[2,'Linh Tinh','Love']]
print(name2)
