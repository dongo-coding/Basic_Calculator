# Máy tính Python đơn giản
print("🧮 Máy Tính Python")
print("Nhập hai số để tính toán:")

first_number = float(input("Số thứ nhất: "))
second_number = float(input("Số thứ hai: "))

print(f"\n📊 Kết quả:")
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} × {second_number} = {first_number * second_number}")
if second_number != 0:
    print(f"{first_number} ÷ {second_number} = {first_number / second_number}")
