# 1, Modules là gì?
# Modules là cách mà chúng ta phân hóa chương trình ra các nhánh nhỏ cho dễ quản lý và gọi lại chúng khi nào cần, 
# như thế chương trình của chúng ta sẽ có tính tái sử dụng, bảo trì cao.
# 2, Modules trong Python.
# Import
# Để import một module có vào trong file hiện tại thì mọi người sử dụng từ khóa import với cú pháp như sau:

# import module1, module2,...
# Trong đó: module1, module2,... là các modules mà các bạn muốn import vào file hiện tại.

import math
a = 3.2
# làm tròn lên 1 số
print(math.ceil(a))
# làm tròn xuống 1 số
print(math.floor(a))

# from - import
# Giả sử trong một trường hợp nào đó khi bạn không muốn sử dụng hết toàn bộ module mà chỉ muốn sử dụng một số thứ 
# trong đó mà thôi thì sẽ phải làm sao? Trong trường hợp này chúng ta sử dụng từ khóa from...import theo cú pháp như sau:

# from modules import something, something2,...

# Trong đó:
# modules là tên của module mà các bạn muốn import.
# something1,somthing2,... là những thứ mà các bạn muốn sử dụng ở trong modules. 
# Nếu như bạn muốn import tất cả những gì trong modules có và cho phép thì bạn sử dụng keyword *.

from math import ceil
a = 3.2

print(ceil(a))

from math import *
a = 3.2

print(ceil(a)) 
print(floor(a))



