# 1, map().
# Hàm map này có tác dụng duyệt qua tất cả các phần tử của một hoặc nhiều list, dictionary hoặc tương tự như thế, 
# sử dụng đơn giản với cú pháp như sau:

# map(function, iterable1, iterable2 ,...)
# Trong đó:

# function là hàm xử lý logic qua mỗi lần lặp giá trị trong interable1, ......
# interable1, interable2 là các list, dict ,... các bạn cần lặp.
# Hàm map sẽ trả về một map object chứa các kết quả sau khi thực thi.

# VD: nhân đôi giá trị của tất cả các phần tử trong list.

def mutiply(x):
    return x * x


result = map(mutiply, [1, 2, 3, 4])

print(list(result)) # [1, 4, 9, 16]

# Và function kia bạn có thể khai báo dưới dạng lambla cho gọn như sau:

result = map(lambda x: x * x, [1, 2, 3, 4])

print(list(result))  # [1, 4, 9, 16]
# VD: map đối với 2 list truyền vào.

result = map(lambda x, y: x + " " + y, ['red', 'blue'], ['green', 'black'])

print(list(result))  # ['red green', 'blue black']

# 2, filter().
# Hàm này cũng có tác dụng duyệt qua các phần tử trong list, dict,... nhưng khác với map là hàm này sẽ chỉ trả về 
# những giá trị mà điều kiện trong function chấp nhận (có nghĩa là True).

# Cú pháp:

# filter(function, iterable)
# Trong đó:

# function là hàm xử lý logic qua mỗi lần lặp giá trị trong interable, ......
# interable là các list, dict ,... các bạn cần lặp.
# Hàm filter sẽ trả về một map object chứa các kết quả sau khi thực thi.

# VD: filter các giá trị không chia hết cho 2.

result = filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 22])

print(list(result))  # [1, 3, 5, 7, 9]