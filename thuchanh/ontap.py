# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# Bài 1: In bảng cửu chương từ a đến b
def bang_cuu_chuong(a, b):
    if a < b:
        start = a
        end = b
    else:
        start = b
        end = a

    for i in range(start, end + 1):
        print(f"\nBảng cửu chương {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")


# Bài 2: Kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to():
    n = int(input("Nhập n: "))

    if la_so_nguyen_to(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")


# Bài 3: Liệt kê số nguyên tố < n
def liet_ke_so_nguyen_to():
    n = int(input("Nhập n: "))

    print("Các số nguyên tố <", n, "là:")
    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i, end=" ")


# Bài 4: Đếm số nguyên tố < n
def dem_so_nguyen_to():
    n = int(input("\nNhập n: "))
    dem = 0

    for i in range(2, n):
        if la_so_nguyen_to(i):
            dem += 1

    print("Có", dem, "số nguyên tố <", n)


# Bài 5: Liệt kê các ước số nguyên tố của n
def uoc_so_nguyen_to():
    n = int(input("Nhập n: "))

    print("Các ước số nguyên tố của", n, "là:")

    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            print(i, end=" ")


# ================== CHƯƠNG TRÌNH CHÍNH ==================

# Bài 1
a, b = map(int, input("Nhập a,b: ").split(","))
bang_cuu_chuong(a, b)

# Bài 2
kiem_tra_so_nguyen_to()

# Bài 3
liet_ke_so_nguyen_to()

# Bài 4
dem_so_nguyen_to()

# Bài 5
uoc_so_nguyen_to()
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# Bài 1: In bảng cửu chương từ a đến b
def bang_cuu_chuong(a, b):
    if a < b:
        start = a
        end = b
    else:
        start = b
        end = a

    for i in range(start, end + 1):
        print(f"\nBảng cửu chương {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")


# Bài 2: Kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to():
    n = int(input("Nhập n: "))

    if la_so_nguyen_to(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")


# Bài 3: Liệt kê số nguyên tố < n
def liet_ke_so_nguyen_to():
    n = int(input("Nhập n: "))

    print("Các số nguyên tố <", n, "là:")
    for i in range(2, n):
        if la_so_nguyen_to(i):
            print(i, end=" ")


# Bài 4: Đếm số nguyên tố < n
def dem_so_nguyen_to():
    n = int(input("\nNhập n: "))
    dem = 0

    for i in range(2, n):
        if la_so_nguyen_to(i):
            dem += 1

    print("Có", dem, "số nguyên tố <", n)


# Bài 5: Liệt kê các ước số nguyên tố của n
def uoc_so_nguyen_to():
    n = int(input("Nhập n: "))

    print("Các ước số nguyên tố của", n, "là:")

    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            print(i, end=" ")


# CHƯƠNG TRÌNH CHÍNH 

# Bài 1
a, b = map(int, input("Nhập a,b: ").split(","))
bang_cuu_chuong(a, b)

# Bài 2
kiem_tra_so_nguyen_to()

# Bài 3
liet_ke_so_nguyen_to()

# Bài 4
dem_so_nguyen_to()

# Bài 5
uoc_so_nguyen_to()