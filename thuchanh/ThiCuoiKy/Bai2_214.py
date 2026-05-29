import math
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

n = int(input("Nhập số nguyên dương n: "))

if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")


dem = 0

for i in range(2, n):
    if la_so_nguyen_to(i):
        dem += 1

print("Số lượng số nguyên tố nhỏ hơn", n, "là:", dem)


print("Các ước số nguyên tố của", n, "là:")

for i in range(1, n + 1):
    if n % i == 0 and la_so_nguyen_to(i):
        print(i, end=" ")