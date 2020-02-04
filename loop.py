# Vòng lặp trong Python

# Vòng lặp for ở trong Python có tác dụng lặp các biến dữ liệu có trong list , tuple hoặc string,... 
# Sử dụng cú pháp như sau:

# for variable in data:
#     # code
# Trong đó:

# variable là các biến tạm dùng để chứa dữ liệu sau mỗi lần lặp.
# data là một list, tuple hoặc string,... chứa giá trị cần lặp.

#Example: 
name = 'Nguyen Van Chinh'

for i in name:
    print(i)

for i in range(0,10):
    for j in range(i,10):
        print(j, end = " ")
    print ("")

# Vòng lặp while trong Python dùng để lặp các dữ liệu mà giá trị ngừng có của nó là chưa biết trước.

# Cú pháp sử dụng:

# while condition:
#     # code
# Trong đó, condition là điều kiện quyết định vòng lặp while có được chạy hay không. 
# Nếu condition trả về giá trị là True thì vòng lặp while mới được thực thi, 
# và ngược lại thì nó sẽ không thực thi nếu condition trả về False.

#===============================
i = 1;
while(i <= 10):
    print(i)
    i += 1

#================================
i = 1

while(i <= 10):
    j = 1
    while (j <= 10 - i):
        print(j, end = " ")
        j += 1
    print("")
    i += 1

# Các từ khóa tác động đến vòng lặp.
# Thông thường trong một số trường hợp vòng lặp của chúng ta sẽ có thể không cần thực thi code 
# trong một số vòng lặp cụ thể hay là cần nhảy lần vòng lặp đó và thực thi các lần lặp tiếp theo, 
# và để làm được điều đó thì trong Python có hỗ trợ chúng ta 3 keyword để tác động đến vòng lặp là:

# break - giúp chúng ta chấm dứt vòng lặp tại thời điểm nó xuất hiện
#  và các code cùng cấp phía sau nó sẽ không được thực thi nữa.

# continue - giúp chúng ta nhảy qua lần lặp hiện tại và chuyển đến lần lặp tiếp theo, 
# các code cùng cấp phía sau nó cũng sẽ không được thực hiện.

#================================
i = 1

while(i <= 10):
    print(i)
    if i == 5 :
        break
    i += 1
#================================
for i in name:
    if i == "n":
        continue
    print(i, end=" ")
