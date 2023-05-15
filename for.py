fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# Lặp chữ cái trong quantrimang
for letter in "quantrimang":
    print(letter)

chuoi = ["cam", "chuoi", "man"]
for c in chuoi:
    print(c)

# Tính tổng tất cả các số trong danh sách A
# Danh sách A
A = [1, 3, 5, 9, 11, 2, 6, 8, 10]
print("Danh sách A", A)

tong = 0
for a in A:
    tong += a

print("Tổng các số là", tong)

# =================================
# Lệnh break trong for
# =================================

ds_trai_cay = ["cam", "dao", "xa", "", "bap", ""]

for trai_cay in ds_trai_cay:
    if trai_cay == "":
        break
    print(trai_cay)
print("Nội dung ngoài vòng lặp for")

# =================================
# Lệnh continue trong for
# =================================
a = ["quan", "tri", "mang", ".", "com"]
for chu in a:
    if chu == ".":
        continue
    print(chu)
print("Nội dung ngoài vòng lặp for")

# =================================
# Lệnh pass trong for
# Các lệnh trong vòng lặp for thường không thể để trống,
# nhưng nếu vì một lý do nào đó bạn mới chỉ lên ý tưởng cho vòng lặp for mà chưa có nội dung bên trong,
# lúc này hãy sử dụng lệnh pass để "đặt chỗ" cho những khối code mà mình chưa nghĩ ra.
# =================================
for x in "QuanTriMang":
    pass
print("Nội dung ngoài vòng lặp for")

# =================================
# Hàm range()
# range(so_bat_dau, so_ket_thuc, khoang_cach_2_so)
# =================================
for i in range(20):
    print("Hello, be Son")
print("Nội dung ngoài vòng lặp for")

# Hàm range() không lưu tất cả các giá trị trong bộ nhớ
# mà nó lưu giá trị bắt đầu, giá trị kết thúc và khoảng cách giữa hai số từ đó tạo ra số tiếp theo trong dãy.

print(range(9), type(range(9)))
print(list(range(9)), type(list(range(9))))

chuoi = ["bố", "mẹ", "em"]
for i in range(len(chuoi)):
    print("Anh yeu ", chuoi[i])

# =================================
# Vòng lặp for lồng nhau
# =================================
tinhtu = ["đỏ", "to", "ngon"]
qua = ["táo", "chuối", "cherry"]
for q in qua:
    for t in tinhtu:
        print(q, t)

# =================================
# Kết hợp for với else
# =================================
B = [0, 2, 4, 5]

for b in B:
    print(b)
else:
    print("Đã hết số.")


# Lặp dãy từ 0 đến 10
for num in range(10):
    # Lặp trên các thừa số của một số trong dãy
    for i in range(2, num):
        # Xác định thừa số đầu tiên (phép chia có số dư bằng 0)
        if num % i == 0:
            # Ước lượng thừa số thứ 2
            j = num / i
            print("%d bằng %d * %d" % (num, i, j))
            break  # Dừng vòng for hiện tại, chuyển đến số tiếp theo trong vòng for đầu tiên
    else:  # Phần else trong vòng lặp
        print(num, "là số nguyên tố")

x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
        print(x)
