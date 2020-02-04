# Các toán tử cơ bản trong Python
# 1, Toán tử số học - Arithmetic Operators.

# +	Toán tử cộng các giá trị lại với nhau	a + b = 12
# -	Toán tử trừ các giá trị lại với nhau	a - b = -2
# '*	Toán tử nhân các giá trị lại với nhau	a * b = 42'
# /	Toán tử chia các giá trị cho nhau	a / b = 0.7142857142857143
# %	Toán tử chia lấy phần dư 	a % b = 5
# '**	Toán tử mũ. 	a ** b = 78125'
# '//	Toán tử chia làm tròn xuống. a // b = 0'

# VD:
# 0,57 => 0
# 0.9 => 0
# -07 => -1
# -0.1 => -1

# 2, Toán tử Quan hệ.

# Dạng toán tử này dùng để so sánh các giá trị với nhau kết quả của nó sẽ trả về là True nếu đúng
# và False nếu sai. Và nó thường được dùng trong các câu lệnh điều kiện.

# Trong Python thì nó cũng tồn tại 6 dạng toán tử quan hệ cơ bản như sau:

# ==	So sánh giá trị của các đối số xem có bằng nhau hay không.
#     Nếu bằng nhau thì kết quả trả về sẽ là True và ngược lại sẽ là False.
# a == b  // False


# '!=	So sánh giá trị của các đối số xem có khác nhau hay không.
# Nếu khác nhau thì kết quả trả về sẽ là True và ngược lại sẽ là False.	
# a != b //True


# <	Dấu < đại diện cho phép toán nhỏ hơn, 
# nếu đối số 1 nhỏ hơn đối số 2 thì kết quả sẽ trả về là True và ngược lại sẽ là False.	
# a < b //True


# >	Dấu > đại diện cho phép toán lớn hơn, 
# nếu đối số 1 lớn hơn đối số 2 thì kết quả sẽ trả về là True và ngược lại sẽ là False.	
# a > b //False


# <=	Dấu > đại diện cho phép toán nhỏ hơn hoặc bằng, 
# nếu đối số 1 nhỏ hơn hoặc bằng đối số 2 thì kết quả sẽ trả về là True và ngược lại sẽ là False.
# a <= b //True


# >=	Dấu > đại diện cho phép toán lớn hơn hoặc bằng, 
# nếu đối số 1 lớn hơn hoặc bằng đối số 2 thì kết quả sẽ trả về là True và ngược lại sẽ là False.	
# a>= b //False

# 3, Toán tử gán.
# Toán tử gán là toán tử dùng đế gán giá trị của một đối tượng cho một đối tượng khác. 
# Và trong Python thì nó cũng được thể hiện giống như các ngôn ngữ khác. 
# Và dưới đây là 8 toán tử nằm trong dạng này mà Python hỗ trợ.

#  =	Toán tử này dùng để gán giá trị của một đối tượng cho một giá trị	c = a (lúc này c sẽ có giá trị = 5)
# +=	Toán tử này cộng rồi gắn giá trị cho đối tượng	c += a (tương đương với c = c + a)
# -=	Toán tử này trừ rồi gắn giá trị cho đối tượng	c -= a (tương đương với c = c - a)
# '*=	Toán tử này trừ rồi gắn giá trị cho đối tượng	c *= a (tương đương với c = c * a)
# /=	Toán tử này chia rồi gắn giá trị cho đối tượng	c /= a (tương đương với c = c / a)
# %	Toán tử này chia hết rồi gắn giá trị cho đối tượng	c %= a (tương đương với c = c % a)
# '**=	Toán tử này lũy thừa rồi gắn giá trị cho đối tượng	c **= a (tương đương với c = c ** a)
# '//=	Toán tử này chia làm tròn rồi gắn giá trị cho đối tượng	c //= a (tương đương với c = c // a)

# 4, Toán tử logic.
# Toán tử logic trong Python hoàn toàn giống như các ngôn ngữ khác. Nó gồm có 3 kiểu cơ bản như sau:

# and	Nếu 2 vế của toán tử này đều là True thì kết quả sẽ là True và ngược lại nếu 1 trong 2 vế là False 
# thì kết quả trả về sẽ là False.

# or	Nếu 1 trong 2 vế là True thì kết quả trả về sẽ là True và ngược lại nếu cả 2 vế là False 
# thì kết quả trả về sẽ là False.

# not	Đây là dạng phủ định, nếu biểu thức là True thì nó sẽ trả về là False và ngược lại.

# 5, Toán tử biwter.
# Toán tử này thực hiện trên các bit của các giá trị. Hãy tưởng tượng mình có 2 biến a = 12 và b = 15 
# nhưng nếu chúng ta convert chúng sang hệ nhị phân thì 2 biến này sẽ có giá trị như sau: 
# a = 00001100 và b = 00001111.

# &	(a & b) = 12 (00001100)
# |	(a | b) = 14 (00001111)
# ^	(a ^ b) = 2 (00000010) 
# ~	(-a) = -13 (00001101)
# <<	a<<a = 49152
# >>	a>>a = 0

# 6, Toán Tử khai thác.

# Toán tử này thường được dùng để kiểm tra xem 1 đối số có nằm trong 1 tập hợp đối số hay không (list). 
# Trong Python hỗ trợ chúng ta 2 dạng toán tử như sau:

# Giả sử: a = 4, b = [1,5,7,6,9]

# in	Nếu 1 đối số thuộc một tập đối số nó sẽ trả về True và ngược lại/	a in b //False
# not in	Nếu 1 đối số không thuộc một tập đối số nó sẽ trả về True và ngược lại/	a not in b //True

# 7, Toán tử xác thực.
# Dạng Toán tử này dùng để xác thực hai giá trị xem nó có bằng nhau hay không. Và trong Python hỗ trợ chúng ta 2 dạng sau:

# Giả sử: a = 4, b =5

# is	Toán tử này sẽ trả về True nếu a == b và ngược lại	 a is b //False
# not is	Toán tử này sẽ trả về True nếu a != b và ngược lại	a is not b //True