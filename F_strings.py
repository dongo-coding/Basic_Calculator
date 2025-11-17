# Thông tin cá nhân
full_name = "Nguyễn Văn Minh"
age = 16
math_score = 8.5
literature_score = 9.0

print(f"👋 Xin chào! Tôi là {full_name}")
print(f"🎂 Tôi {age} tuổi")
print(f"📊 Điểm Toán: {math_score}, Điểm Văn: {literature_score}")

# Tính toán trong f-string
print(f"📈 Điểm trung bình: {(math_score + literature_score) / 2}")


# Số thập phân
price = 125000.789
print(f"💰 Giá: {price:.2f} VNĐ")  # 2 chữ số thập phân
print(f"💰 Giá: {price:,.0f} VNĐ")  # Thêm dấu phẩy, không thập phân

# Phần trăm
accuracy_rate = 0.85
print(f"✅ Tỷ lệ đúng: {accuracy_rate:.1%}")  # Chuyển thành %

# Số nguyên với độ rộng cố định
order_number = 7
print(f"📋 Thứ tự: {order_number:03d}")  # Thêm số 0 phía trước


from datetime import datetime, date

# Thời gian hiện tại
now = datetime.now()
today = date.today()

# Các cách format khác nhau
print(f"📅 Hôm nay: {today}")
print(f"⏰ Bây giờ: {now}")
print(f"📅 Ngày đẹp: {today:%d/%m/%Y}")
print(f"⏰ Giờ: {now:%H:%M:%S}")
print(f"🌅 Thời điểm: {now:%d tháng %m năm %Y, %H:%M}")

# Ngày trong tuần (tiếng Việt)
days_of_week = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
day = days_of_week[today.weekday()]
print(f"📆 Hôm nay là {day}")
