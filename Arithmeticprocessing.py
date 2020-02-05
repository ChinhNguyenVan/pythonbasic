# 1, abs().
# Hàm này có tác dụng trả về giá trị tuyệt đối của một số.

# Lưu ý: Hàm này không nằm trong module math, nên các bạn không cần phải import modules math.

# Cú pháp:

# abs(number)
# Trong đó, number là số mà các bạn muốn chuyển đổi.

# VD:

number = -5
print(abs(number))
# Kết quả: 5

number = -19.6
print(abs(number))
# Kết quả: 19.6
# 2, fabs().
# Hàm này có tác dụng trả về giá trị tuyệt đối của một số. Nhưng nó sẽ có khác với hàm abs() ở trên là hàm này sẽ chỉ chấp nhận chuyển đổi được kiểu số nguyên (integer) và số thực (float) trong khi hàm abs() chuyển đổi được cả complex number.

# Cú pháp:

# math.fabs(number)
# Trong đó, number là số mà các bạn muốn chuyển đổi.

# VD:

import math

number = -5
print(math.fabs(number))
# Kết quả: 5

number = -19.6
print(math.fabs(number))
# Kết quả: 19.6
# 3, ceil().
# Hàm này có tác dụng chuyển đổi một số về dạng số nguyên của nó và số nguyên đó phải lớn hơn hoặc bằng số ban đầu. 
# Nói một cách đơn giản thì hàm này có tác dụng làm tròn lên 1 số.

# Cú pháp:

# math.ceil(number)
# Trong đó, number là số mà các bạn muốn chuyển đổi.

# VD:

import math

number = 5.2
print(math.ceil(number))
# Kết quả: 6

number = 19.6
print(math.ceil(number))
# Kết quả: 20

number = -19.6
print(math.ceil(number))
# Kết quả: -19
# 4, exp().
# Hàm này có tác dụng trả về kết quả ex, trong đó x là số mà các bạn cần tính.

# VD:

import math

number = 5
print(math.exp(number))
# Kết quả: 148.4131591025766
# 5, floor().
# Hàm này có tác dụng làm tròn một số về dạng số nguyên nhỏ hơn hoặc bằng số ban đầu. 
# Nói cách khác thì là làm tròn xuống một số.

# VD:

import math

number = 5.3
print(math.floor(number))
# Kết quả: 5

number = 19.6
print(math.floor(number))
# Kết quả: 19

number = -19.6
print(math.floor(number))
# Kết quả: -20
# 6, log().
# Hàm này sẽ trả về kết quả logarithm x, với x là số cần chuyển và x > 0.

# VD:

import math

number = 5.3
print(math.log(number))
# Kết quả: 1.667706820558076

number = 19.6
print(math.log(number))
# Kết quả: 2.975529566236472
# 7, log10().
# Hàm này tương tự như hàm log(), nhưng là dạng logarithm cơ số 10.

# VD:

import math

number = 5.3
print(math.log10(number))
# Kết quả: 0.724275869600789

number = 19.6
print(math.log10(number))
# Kết quả: 1.2922560713564761
# 8, max().
# Hàm này có tác dụng trả về số lớn nhất trong các số được truyền vào.

# Lưu ý: Hàm này không nằm trong module math, nên các bạn không cần phải import modules math.

# VD:

x, y = 5, 9
print(max(x, y))
# Kết quả: 9

x, y, z = 5, 1, 3
print(max(x, y, z))
# Kết quả: 5
# 9, min().
# Hàm này có tác dụng trả về số nhỏ nhất trong các số được truyền vào.

# Lưu ý: Hàm này không nằm trong module math, nên các bạn không cần phải import modules math.

# VD:

x, y = 5, 9
print(min(x, y))
# Kết quả: 5

x, y, z = 5, 1, 3
print(min(x, y, z))
# Kết quả: 1
# 10, modf().
# Hàm này có tác dụng chuyển đổi một số về một tuple. Tuple này chứa phần thập phân và phần nguyên của số đó, 
# lưu ý tất cả các giá trị trong tuple này đều ở dạng float. 

# VD:

import math

x = 5.278
print(math.modf(x))
# Kết quả: (0.2779999999999996, 5.0)

x = -102.69874
print(math.modf(x))
# Kết quả: (-0.6987400000000008, -102.0)

# 11, pow().
# Hàm này có tác dụng trả về kết quả của phép xy, với x là tham số thứ nhất, y là tham số thứ 2.

# VD:

import math

x, y = 5, 2
print(math.pow(x, y))
# Kết quả: 25.0

x, y = 10, 5
print(math.pow(x, y))
# Kết quả: 100000.00

# 12, round().
# Hàm này có tác dụng làm tròn số về dạng cần thiết.

# Lưu ý: Hàm này không nằm trong module math, nên các bạn không cần phải import modules math.

# Cú pháp:

# math.round(number, count = 0)
# Trong đó:

# number là số mà các bạn cần làm tròn.
# count là số mà các bạn muốn làm tròn sau dấu phẩy. Mặc định thì count = 0.
# VD: 

x = 5.15742
print(round(x))
# Kết quả: 5

x = 10.677781
print(round(x, 2))
# Kết quả: 10.68
# 13, sqrt().
# Hàm này có tác dụng trả về căn bậc 2 của một số, với điều kiện số đó phải lớn hơn 0.

# VD:

import math

x = 9
print(math.sqrt(x))
# Kết quả: 3.0

x = 10.677781
print(math.sqrt(x))
# Kết quả: 3.267687408550579
# 14, acos().
# Hàm này có tác dụng tính cosine của một số. Với điều kiện số đó phải nằm trong khoảng: -1<= x <=1.

# VD:

import math

x = 1
print(math.acos(x))
# Kết quả: 0.0

x = 0.5
print(math.acos(x))
# Kết quả: 1.0471975511965979
# 15, cos().
# Hàm này cũng trả về cosine của một số, nhưng số này được tính theo radian.

# VD:

import math

x = 1
print(math.cos(x))
# Kết quả: 0.5403023058681398

x = 0.5
print(math.cos(x))
# Kết quả: 0.8775825618903728
# 16, asin().
# Hàm này có tác dụng trả về sine của một số. Với điều kiện số đó phải nằm trong khoảng: -1<= x <=1.

# VD:

import math

x = 1
print(math.asin(x))
# Kết quả: 1.5707963267948966

x = 0.5
print(math.asin(x))
# Kết quả: 0.5235987755982989
# 17, sin().
# Hàm này cũng trả về sine của một số, nhưng số này được tính theo radian.

# VD:

import math

x = 1
print(math.sin(x))
# Kết quả: 0.8414709848078965

x = 0.5
print(math.sin(x))
# Kết quả: 0.479425538604203
# 18, atan() - tan().
# Tương tự như với asin() - sin() và acos() - cos() ta cũng có atan() và tan() với chức năng là tính tangent của một số. 

# VD:

import math

x = 1
print(math.atan(x))
# Kết quả: 0.7853981633974483

print(math.tan(x))
# Kết quả: 1.5574077246549023
# 19, radians().
# Hàm này có tác dụng chuyển đổi từ độ sang radians.

# VD:

import math

x = 1
print(math.radians(x))
# Kết quả: 0.017453292519943295

x = 90
print(math.radians(x))
# Kết quả: 1.5707963267948966