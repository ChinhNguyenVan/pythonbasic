# Khai báo hàm trong Python.
# Để khai báo một hàm trong Python thì chúng ta sử dụng keyword def với cú pháp như sau:

# def ten_ham(param...):
#     #code
# Trong đó:

# ten_ham là tên của hàm mà bạn muốn đặt. Lưu ý: Tên hàm không được bắt đầu bằng số và không được chứa 
# các ký tự đặc biệt trừ ký tự _ param... là các tham số bạn muốn truyền vào hàm, 
# nếu không có tham số thì để trống trường này.

def say():
    print("Welcome to Chinh Nguyen Van")
def tinhtong(a,b):
    print("Sum =" + str(a+b))

# Gọi hàm.
# Để gọi một hàm đã được khai báo rồi, thì chúng ta sử dụng cú pháp sau:

# ten_ham()
# #hoặc
# ten_ham(param...)
# Trong đó:

# ten_ham là tên của hàm là chúng ta muốn gọi.
# param... là các tham số chúng ta muốn truyền vào trong hàm.

say()
tinhtong(5,6)
tinhtong('Hello',' World')
tinhtong(3.2,4.8)

# Hàm có kết quả trả về.
# Trong trường hợp bạn muốn sử dụng kết quả của hàm vừa tính để thực hiện các mục đíc khác. 
# Thì bạn chỉ cần thêm keyword return trước kết quả bạn muốn trả về.

def SumAll(c,d):
    return c + d

c = SumAll(4,5)
print('Tong la: ' + str(c))

# Phạm vi của biến trong hàm.
# Khi một biến được khai báo ở trong hàm thì nó chỉ có thể được sử dụng ở trong hàm đó thôi.

e = "Hello Guy!"
def say(e):
    e = "Toi choi lien minh huyen thoai"
    print(e)

say(e)

print(e)

#chúng ta cũng không thể nào thay đổi giá trị của biến (biến bình thường) mà tác động ra ngoài hàm được 
# Nhưng nếu như biến mà có kiểu dữ liệu là list thì chúng ta lại có thể là được điều đó.
an = [5, 10, 15]
def change(an):
    an[0] = 1000
    print(an)

change(an)

print(an)

# Biến Global.
# Ngoài những cách hoạt động của biến mình đã trình bày ở phần 6 ra thì chúng ta còn có 1 cách nữa để có thể tác động đến các biến bên ngoài hàm khi đang ở trong hàm. Đó là sử dụng global variable - biến toàn cầu, khi một biến là global thì chúng ta có thể gọi và tác động đến nó từ bất kỳ đâu trong chương trình.

# Để khai báo một biến là global thì chúng ta chỉ cần thêm keyword global trước tên của nó như sau:

# global tenbien

aa = "Hello Guy!"
def say():
    global aa
    aa = "Mua xuan den roi"
    print(aa)

say()

print(aa)

# Truyền vô số tham số vào hàm.
# Trên thực tế, không phải lúc nào chúng ta cũng biết được chính xác số lượng biến truyền vào trong hàm. 
# Chính vì thế trong Python có cũng cấp cho chúng ta khai báo một param đại diện cho các biến truyền vào 
# hàm bằng cách thêm dấu * vào trước param đó.

def get_sum(*num):
    tmp = 0
    # duyet cac tham so
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)

print(result)