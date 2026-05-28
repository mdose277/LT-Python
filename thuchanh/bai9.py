# Nhập chiều dài, chiều rộng và chiều cao
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))

# Nhập số lẻ cần hiển thị
sole = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính diện tích đáy
dien_tich = dai * rong

# Tính thể tích khối
the_tich = dai * rong * cao

# In kết quả - Cách 1
print("Cách 1: Diện tích đáy hình chữ nhật =",
      round(dien_tich, sole), "cm\u00b2")

print("Cách 1: Thể tích hình khối =",
      round(the_tich, sole), "cm\u00b3")

# In kết quả - Cách 2
print(f"Cách 2: Diện tích đáy hình chữ nhật = {dien_tich:.{sole}f} cm\u00b2")

print(f"Cách 2: Thể tích hình khối = {the_tich:.{sole}f} cm\u00b3")