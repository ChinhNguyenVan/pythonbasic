# Input và Đọc ghi file trong Python

# 1, Input.
# Trong Python có cung cấp cho chúng ta hàm input để nhận dữ liệu từ người dùng nhập vào trong commandline. 
# Sử dụng với cú pháp như sau:

# input(something)
# Trong đó, something là nội dung mà bạn muốn hiển thị trước khi người dùng nhập dữ liệu. 
# Và giá trị mà hàm này trả về chính là giá trị mà người dùng nhập vào.

print("Hello guy!")
age = input("How old are you? ")
print("age: " + age)

# 2, Đọc ghi file.
# File là một thứ rất cần thiết trong các dự án, ví dụ như chúng ta cần phải ghi log ra một file để sau này có thể kiểm soát được.... Và ngôn ngữ lập trình nào cũng hỗ trợ chúng ta làm việc với file.

# Mở file.
# Để mở file trong Python chúng ta sử dụng hàm open với cú pháp như sau:

# open(filePath, mode, buffer)
# Trong đó:

# filePath là đường dẫn đến địa chỉ của file.
# mode là thông số thiết lập chế độ chúng ta mở file được cấp những quyền gì? 
# Mặc định mode sẽ bằng r(xem các mode ở dưới). 
# Buffer là thông số đệm cho file mặc định thì nó sẽ là 0.



# Đóng file.
# Để đóng một file đang được mở, thì chúng ta sử dụng phương thức close() với cú pháp như sau:

# fileObject.close()
# Trong đó, fileObject là đối tượng mà chúng ta thu được khi sử dụng hàm open().

# Để đảm bảo quy chế đóng mở và giải phóng bộ nhớ cho chương trình thì các bạn phải luôn 
# nhớ đống file khi kết thúc phiên làm việc.



# Đọc file.
# Sau khi đã mở được file ra rồi, để đọc được file thì chúng ta sử dụng phương thức read với cú pháp:

# fileObject.read(length);
# Trong đó:

# fileObject là đối tượng mà chúng ta thu được khi sử dụng hàm open().
# length là dung lượng của dữ liệu mà chúng ta muốn đọc, nếu để trống tham số này thì nó sẽ đọc hết file 
# hoặc nếu file lớn quá thì nó sẽ đọc đến khi giới hạn của bộ nhớ cho phép.

#Example
# mo file
file = open('README.md')
# doc file
data = file.read();
# dong file
file.close()
# in du lieu doc duoc
print(data)

# Ghi file.
# Để ghi được file thì bạn phải chắc chắn là đang mở file ở các chế độ cho phép ghi. Và sử dụng phương thức write với cú pháp sau:

# fileObject.write(data)
# Trong đó:

# fileObject là đối tượng mà chúng ta thu được khi sử dụng hàm open().
# data là dữ liệu mà chúng ta muốn ghi vào trong file.

# mo file o che do ghi
file = open('README.md','w')
# ghi file
file.write('NGUYEN VAN CHINH')
# dong file
file.close()

# Các thuộc tính trong file.
# Nếu như bạn cần biết thêm các thông số của file hiện tại thì bạn có thể tham khảo thêm các thuộc tính trong object file mà Python đã cung cấp sẵn cho chúng ta. Các thuộc tính như sau:

# Trong các trường hợp dưới đây: giả sử file là kết quả thu được từ hàm open().

# Thuộc tính	Chú thích
# file.name	Trả về tên của file đang được mở.
# file.mode	Trả về chế độ mode của file đang được mở.
# file.closed	Trả về true nếu file đã được đóng, và false nếu file chưa đóng.
# VD: Mình sẽ in ra thông số của file readme.md ở trên.

# file = open('readme.md','w')
# print( file.name )
# # readme
# print( file.mode )
# # w
# print( file.closed )
# # False
# file.close()
