dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
sole = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính toán
dien_tich_day = dai * rong
the_tich = dien_tich_day * cao

# Xuất kết quả
print(f"Diện tích đáy hình chữ nhật = {round(dien_tich_day, sole)} cm\u00b2")
print(f"Thể tích hình khối = {round(the_tich, sole)} cm\u00b3")


