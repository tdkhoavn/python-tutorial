from decimal import Decimal

# Các kiểu dữ liệu số trong Python
print(type(9))
print(type(2.5))
print(type(8 + 2j))

print(isinstance(8 + 2j, complex))
print(isinstance(8, int))


# Output: 187
print(0b10111011)

# Output: 257 (250 + 7)
print(0xFA + 0b111)

# Output: 15
print(0o17)

# =================================
# Chuyển đổi giữa các kiểu số trong Python
# =================================
print(2 + 3.0)
print(2 + 3)

print(int(3.6))
print(int(-1.2))
print(complex("2+3j"))

# =================================
# Mô-đun Decimal trong Python
# =================================
print((1.1 + 2.2) == 3.3)
print((Decimal(1.1) + Decimal(2.2)) == Decimal(3.3))
