#01

name = input("Tên của bạn: ")
age = int(input("Tuổi: "))
hobby = input("Sở thích: ")

print("\n" + "🌟" * 40)
print(f"{'🎭 THÔNG TIN CÁ NHÂN':^40}")
print("🌟" * 40)
print(f"👤 Tên: {name}")
print(f"🎂 Tuổi: {age} tuổi")
print(f"❤️ Sở thích: {hobby}")
print(f"📅 Năm sinh: {2024 - age}")
print("🌟" * 40)
print("✨ Chúc bạn học Python vui vẻ! ✨")

#In thông tin cá nhân đẹp


#02

bill_amount = float(input("Số tiền hóa đơn (VNĐ): "))
tip_rate = float(input("Tỷ lệ tip (%, vd: 10): ")) / 100
tip_amount = bill_amount * tip_rate
total_amount = bill_amount + tip_amount
print(f"Tổng số tiền phải trả bao gồm tiền tip là : {total_amount}") 

#Tính tổng tiền bao gồm luôn tiền tip


#03

