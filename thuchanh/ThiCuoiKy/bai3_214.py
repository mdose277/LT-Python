import math

# -----------------------------------
# 1. Kiểm tra số chính phương
# -----------------------------------

# Lambda kiểm tra số chính phương
so_chinh_phuong = lambda n: math.sqrt(n) == int(math.sqrt(n))

n = int(input("Nhập số nguyên n: "))

if so_chinh_phuong(n):
    print(n, "là số chính phương")
else:
    print(n, "không phải số chính phương")


# -----------------------------------
# 2. Kiểm tra loại tam giác
# -----------------------------------

a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Lambda kiểm tra tam giác hợp lệ
tam_giac_hop_le = lambda a, b, c: a + b > c and a + c > b and b + c > a

if tam_giac_hop_le(a, b, c):

    # Kiểm tra loại tam giác
    if a == b == c:
        print("Đây là tam giác đều")

    elif a == b or a == c or b == c:
        print("Đây là tam giác cân")

    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Đây là tam giác vuông")

    else:
        print("Đây là tam giác thường")

else:
    print("Ba cạnh không tạo thành tam giác")