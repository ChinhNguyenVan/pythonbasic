#1, Các ký tự đặc biệt trong chuỗi.
#Ví dụ:
print("Chinh \"Website\"")

print('Chinh \'Website\' ')

print("hello 'Chinh'")

print("Website\t Toidicode.com")

# \n ngắt xuống dòng và bắt đầu dòng mời.
# \t đẩy nội dung phía sau nó cách 1 tab.
# \a chuông cảnh báo.
# \b xóa bỏ khoảng trắng phía trước nó.

# 2, Fomat chuỗi.
# print("%type" %(binding))
# type là các kiểu dữ liệu các bạn muốn binding và thay thế vào vị trí đó.
# binding là giá trị mà các bạn muốn binding vào vị trí được xác định trong chuỗi.
#TYPE là những kiểu trên
# %c	character
# %s	chuỗi
# %i	số nguyên
# %d	số nguyên
# %u	số nguyên
# %o	bát phân
# %x	thập lục phân (in thường)
# %X	thập lục phân (in hoa)
# %e	số mũ  (với e thường)
# %E	số mũ  (với e hoa)
# %f	số thực
# %g	dạng rút gọn của %f and %e
# %G	dạng rút gọn của %f and %E
#Ví dụ: 
guy = "Ban"
full = "Chao mung %s den voi HUTECH" %(guy)
print(full)

guy = "Ban"
doamin = "HUTECH"
full = "Chao mung %s den voi website %s" %(guy, doamin)
print(full)

# 3, Truy cập tới từng giá trị của chuỗi.
# stringName[index]
# stringName là tên của biến chứa chuỗi, hoặc chuỗi.
# index là vị trí của ký tự bạn muốn lấy ra. Index này hỗ trợ chúng ta truy xuất được cả 2 chiều của chuỗi nếu:
# Tính từ đầu thì nó bắt đầu từ 0.
# Tính từ cuối thì nó bắt đầu từ -1.

# stringName[index]

name = "NGUYEN VAN CHINH"
print(name[0])
print(name[-1])

#stringName[start:end]
# stringName là tên của biến chứa chuỗi, hoặc chuỗi.
# start là vị trí của ký tự bắt đầu lấy, nếu để trống start thì nó sẽ lấy từ 0.
# end là vị trí kết thúc (nó sẽ lấy trong khoảng từ start đến < end), nếu để trống end thì nó sẽ lấy đến hết chuỗi.

#stringName[start:end]

name = "NGUYEN VAN CHINH"

print(name[0:6]) 

print(name[7:10])

print(name[7:]) 

print(name[-5:]) 





