import math

# -----------------------------------
# Lambda kiểm tra số chính phương
# -----------------------------------
so_chinh_phuong = lambda n: math.sqrt(n) == int(math.sqrt(n))

# -----------------------------------
# Lambda kiểm tra số hoàn thiện
# -----------------------------------
so_hoan_thien = lambda n: sum(i for i in range(1, n) if n % i == 0) == n


# -----------------------------------
# In các số chính phương từ 1 -> 10000
# -----------------------------------
print("Các số chính phương từ 1 đến 10000:")

for i in range(1, 10001):
    if so_chinh_phuong(i):
        print(i, end=" ")

print("\n")


# -----------------------------------
# In các số hoàn thiện từ 1 -> 10000
# -----------------------------------
print("Các số hoàn thiện từ 1 đến 10000:")

for i in range(1, 10001):
    if so_hoan_thien(i):
        print(i, end=" ")