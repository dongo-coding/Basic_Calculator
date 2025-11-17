print("=" * 40)
print("🐍 CHÀO MỪNG ĐẾN VỚI PYTHON! 🐍")
print("=" * 40)
print()
print("👋 Xin chào! Tôi là Python!")
print("🎯 Tôi sẽ giúp bạn học lập trình!")
print("🚀 Chúng ta sẽ tạo ra những điều tuyệt vời!")
print("💡 Bắt đầu hành trình thú vị nào!")
print()
print("=" * 40)
print("🎉 CHƯƠNG TRÌNH ĐẦU TIÊN THÀNH CÔNG! 🎉")
print("=" * 40)


# In trên cùng một dòng
print("Hello", end=" ")
print("World!")
# Kết quả: Hello World!

# Thay đổi ký tự phân cách
print("Táo", "Cam", "Chuối", sep=" - ")
# Kết quả: Táo - Cam - Chuối

print("Python", "rất", "thú vị", sep=" ", end="!\n")

# In nhiều thông tin
print("Tên:", "Minh", "Tuổi:", 15, "Lớp:", "10A")
# Kết quả: Tên: Minh Tuổi: 15 Lớp: 10A


# Sử dụng ANSI escape codes để tạo màu
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'  # Kết thúc màu

# Sử dụng màu trong print
print(f"{Colors.RED}🔴 Cảnh báo: Lỗi quan trọng!{Colors.END}")
print(f"{Colors.GREEN}✅ Thành công: Chương trình chạy tốt!{Colors.END}")
print(f"{Colors.BLUE}ℹ️ Thông tin: Python đang hoạt động{Colors.END}")
print(f"{Colors.YELLOW}⚠️ Chú ý: Kiểm tra lại code{Colors.END}")

# Kết hợp màu với f-strings
name = "Python"
print(f"{Colors.PURPLE}🐍 Xin chào từ {name}!{Colors.END}")


# Tạo bảng thông tin học sinh
print("=" * 50)
print(f"{'STT':<5} {'Tên':<15} {'Tuổi':<5} {'Điểm TB':<8}")
print("=" * 50)

student_list = [
    (1, "Nguyễn Văn A", 16, 8.5),
    (2, "Trần Thị B", 15, 9.2),
    (3, "Lê Minh C", 16, 7.8)
]

for order, name, age, score in student_list:
    print(f"{order:<5} {name:<15} {age:<5} {score:<8.1f}")

print("=" * 50)



name = input("Tên của bạn: ")
age = int(input("Tuổi: "))
hobby = input("Sở thích: ")

print("\n" + "🌟" * 40)
print(f"{'🎭 THÔNG TIN CÁ NHÂN':^40}")
print("🌟" * 40)
print(f"👤 Tên: {name}")
print(f"🎂 Tuổi: {age} tuổi")
print(f"❤️ Sở thích: {hobby}")
print(f"📅 Năm sinh: {2025 - age}")
print("🌟" * 40)
print("✨ Chúc bạn học Python vui vẻ! ✨")
