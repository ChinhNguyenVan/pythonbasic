# 1, Dictionary là gì?
# Kiểu dữ liệu dictionary trong Python là một kiểu dữ liệu lưu trữ các giá trị chứa key và value , 
# nhìn một cách tổng quát thì nó giống với Json. Và đối với kiểu dữ liệu này thì các giá trị bên trong 
# nó không được sắp xếp theo một trật tự nào cả.

# Để khai báo một dictionary chúng ta sử dụng cặp dấu {} theo cú pháp sau:

# {key1: value1, key2: value2,..., keyN: valueN}
# Trong đó, key1: value1, key2: value2,..., keyN: valueN là các key và giá trị của kiểu dữ liệu dictionary. Và tên của key thì các bạn phải tuân thủ theo một số quy tắc sau:

# Các phần tử đều phải có key.
# Và Key chỉ có thể là số hoặc chuỗi.
# Key phải là duy nhất, nếu không nó sẽ nhận giá trị của phần tử có key được xuất hiện cuối cùng.
# Key khi đã được khai báo thì không thể đổi được tên.
# Key có phân biệt hoa thường.
# VD: Mình sẽ khai báo một dictionary như sau:

person = {
    'name': 'Nguyen Van Chinh',
    'age': 21,
    'gender': 'male',
    'sologan': 'never give up'
}

# 2, Truy cập đến các phần tử trong dictionary.
# -Để truy cập đến các phần tử trong dictionary thì các bạn sử dụng cú pháp sau:

# dicName[key]

# dicName là tên của của dictionary.
# key là tên của key các bạn muốn lấy ra trong dictionary.

person = {
    'name': 'Nguyen Van Chinh',
    'age': 21,
    'gender': 'male',
    'sologan': 'never give up'
}
print(person)
print(person['name'])
print(person['sologan'])

#Thay đổi giá trị của dictionary.
person = {
    'name': 'Nguyen Van Chinh',
    'age': 21,
    'gender': 'male',
    'sologan': 'never give up'
}
person['age'] = 22
print(person)
#Xóa phần tử trong diction.
person1 = {
    'name': 'Nguyen Van Chinh',
    'age': 21,
    'gender': 'male',
    'sologan': 'never give up'
}
del person1['sologan']
print(person1)

# 3,Dictionary lồng nhau.
person2 = {
    'name': 'Nguyen Van Chinh',
    'age': 21,
    'gender': 'male',
    'sologan': 'never give up',
    'adress' : {
        'number': '12',
        'street': '32',
        'city': 'Ho Chi Minh'
    }
}

print(person2)
print(person2['adress']['city'])
