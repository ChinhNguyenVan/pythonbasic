# Packages trong Python
# 1, Package là gì?
# Package trong Python là một thư mục chứa một hoặc nhiều modules hay các package khác nhau, nó được tạo ra 
# nhằm mục đích phân bố các modules có cùng chức năng hay một cái gì đó, để dễ quản lý source code.

# VD: ví dụ một package views thì nó sẽ chứa các modules liên quan đến views.

# 2, Build package trong Python.
# Để tạo ra một package trong python thì mọi người chỉ cần tạo ra một thư mục, với tên thư mục chính là tên của package 
# và trong thư mục này nhất định phải có một file có tên __init__.py. File __init__.py này nó giống như các constructor,
# và nó sẽ được gọi ra đầu tiên khi chúng ta import package đó.

# Nói lý thuyết có vẻ rườm rà, nên để dễ hiểu hơn thì mọi người có thể tham khảo ví dụ sau.

# VD: Đầu tiên mọi người tạo cho mình một thư mục mới có cấu trúc như sau:

# |demopackage/__init__py
# |main.py
# Bây giờ mọi người mở file __init__.py ra và viết cho mình đoạn code sau vào:

# # __init__.py
# print("Duoc in tu file __init__py")
# Tiếp đó, ở file main.py các bạn import package demopackage vào như sau:

# # main.py
# import demopackage
# Sau đó các bạn chạy file main.py, sẽ thu được kết quả như sau:

# Duoc in tu file __init__py
# Như vậy các bạn đã hiểu về file __init__.py trong package

# 3, Import package.
# Để import các package thì các bạn sử dụng cú pháp giống như đối với modules. 
# Nhưng bây giờ các bạn sẽ phải gọi từ package -> module.

# VD: Trong thư mục demopackage ở ví dụ trên các bạn tạo cho mình file module.py.

# Cấu trúc thư mục:

# |--demopackage/
# |             |--modules.py
# |             └── __init__py
# |--main.py
# Và ở trong file modules.py các bạn tạo cho mình 2 hàm như sau:

# # demopackage/modules.py
# def say_hello():
#     print("Hello!")

# def say_goodbye():
#     print("Goodbye!")
# Lúc này khi muốn import modules.py vào main.py thì mọi người sẽ gọi như sau:

# # main.py
# from demopackage.modules import *
# # Duoc in tu file __init__py

# say_hello()
# # Hello!

# say_goodbye()
# # Goodbye!
# hoặc

# # main.py
# import demopackage.modules
# # Duoc in tu file __init__py

# demopackage.modules.say_hello()
# # Hello!

# demopackage.modules.say_goodbye()
# # Goodbye!
# hoặc

# # main.py
# import demopackage.modules as modules
# # Duoc in tu file __init__py

# modules.say_hello()
# # Hello!

# modules.say_goodbye()
# # Goodbye!
# 4, Package chứa package.
# Đối với package trong Python thì nó cũng có thể chứa 1 hoặc nhiều package khác trong nó, và không dưới hạn số lần chứa đó nhưng các bạn vẫn phải luôn tuân thủ quy tắc của 1 package là phải có file __init__.py. Tức là package a chứa package b và package b lại chưa package c,...

# VD: Cũng với thư mục trong VD ở phần 3 mình sẽ tạo thêm 1 package con nằm trong demopackage có tên là packagechild chứa 2 file childmodule.py và __init__.py như sau:

# Cấu trúc thư mục:

# |--demopackage/
# |             |--modules.py
# |             |--packagechild/
# |                            |-- childmodule.py
# |                            └── __init__py
# |             └── __init__py
# |--main.py
# file childmodules.py:

# # packagechild/childmodule.py
# def say():
#     print("childmodule.py: Hello")
# file __init__.py:

# # packagechild/__init__.py
# print("childpackage __init__.py")
# Lúc này ở file main.py các bạn chỉ cần import theo đúng cấp package.

# # main.py
# from demopackage.packagechild.childmodule import *
# # childpackage __init__.py

# say()
# # childmodule.py: Hello