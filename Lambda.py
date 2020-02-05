# 1, Lambda là gì?
# - Lambda là một anonymous function (hàm ẩn danh) nó có thể khai báo, định nghĩa ở bất kỳ đâu và không có 
# khả năng tái sử dụng.

# - Lambda chỉ tồn tại trong phạm vi của biến mà nó được định nghĩa, vì vậy nếu như biến đó vượt ra ngoài phạm vi 
# thì hàm này cũng không còn tác dụng nữa.

# - Lambda thường được dùng để gán vào biến, hay được gán vào hàm, class như một tham số.

# 2, Khai báo lambda.
# Để khai báo một lambda trong Python chúng ta sử dụng cú pháp sau:

# lambda arguments_list: expression
# Trong đó:

# lambda là keyword bắt buộc.
# arguments_list là các tham số truyền vào lambda.
# expression là các biểu thức xử lý lambda.
# 3, Ví dụ.
# Ví dụ khai báo một lambda function để tính tổng của 2 biến.

add = lambda a, b: a + b

# call lambda

print(add(3, 4)) # 7
# Kiểm tra xem lambda có kiểu dữ liệu là gì

add = lambda a, b: a + b

print(type(add)) # function