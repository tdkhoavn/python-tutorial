# =================================
# Ví dụ: In lần lượt các số nhỏ hơn 8
# =================================

# In và đếm các số từ 0 tới 8:
count = 1
n = 0
while n < 8:
    print("So thu", count, "la", n)
    n += 1
    count += 1
print("Hết rồi!")


# =================================
# Ví dụ: Tính tổng các số
# =================================
n = int(input("Nhap n: "))
tong = 0
i = 1

while i < n:
    tong += i
    i += 1
print("Tổng là", tong)

# =================================
# Lệnh break trong while
# =================================
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# =================================
# Lệnh continue trong while
# =================================
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# =================================
# Kết hợp while với else
# =================================
dem = 0
while dem < 3:
    print("Đang ở trong vòng lặp while")
    dem = dem + 1
else:
    print("Đang ở trong else")

# Ví dụ: Đếm và in các số nhỏ hơn 2
n = 0
while n < 2:
    print(n, "nhỏ hơn 2")
    n = n + 1
else:
    print(n, "không nhỏ hơn 2")
