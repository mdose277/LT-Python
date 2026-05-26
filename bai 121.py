# Bai121.py

def generate_strobo(n, total):

    pairs = [
        ('0', '0'),
        ('1', '1'),
        ('6', '9'),
        ('8', '8'),
        ('9', '6')
    ]

    # trường hợp cơ sở
    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "8"]

    result = []

    middle_list = generate_strobo(n - 2, total)

    for middle in middle_list:

        for a, b in pairs:

            # không cho số đầu là 0
            if n == total and a == '0':
                continue

            result.append(a + middle + b)

    return result


def generate_extended(n, total):

    pairs = [
        ('0', '0'),
        ('1', '1'),
        ('6', '9'),
        ('8', '8'),
        ('9', '6')
    ]

    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "6", "8", "9"]

    result = []

    middle_list = generate_extended(n - 2, total)

    for middle in middle_list:

        for a, b in pairs:

            if n == total and a == '0':
                continue

            result.append(a + middle + b)

    return result


# ==========================
# MAIN
# ==========================

n = int(input("Nhap n (2 <= n <= 10): "))

while n < 2 or n > 10:
    n = int(input("Nhap lai n: "))

# a
print("\n=== STROBOGRAMMATIC ===")

strobo = generate_strobo(n, n)

for x in strobo:
    print(x)

# b
print("\n=== STROBOGRAMMATIC MO RONG ===")

extended = generate_extended(n, n)

for x in extended:
    print(x)
