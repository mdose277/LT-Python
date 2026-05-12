x = int(input("Nhap so tien x: "))
menh_gia = [500,200,100,50,20,10,5,2,1]
tong_to = 0
print(f"So tien {x} duoc doi thanh:")
for tien in menh_gia:
    so_to = x // tien
    x = x % tien 
    tong_to += so_to

    print(f"Loai {tien} gom {so_to} to")
    print("TONG CONG CO",  tong_to,"TO")
