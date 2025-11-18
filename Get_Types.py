age = int(input("Tuổi của bạn: "))
next_year = age + 1

# Số thập phân
height = float(input("Chiều cao (m): "))
weight = float(input("Cân nặng (kg): "))
bmi = weight / (height ** 2)
print(f"Năm sau bạn sẽ {next_year} tuổi")
print(f"BMI của bạn: {bmi:.2f}")

#Nhận số_Numbers

# Cách 1: So sánh string
likes_python = input("Bạn có thích học Python không? (có/không): ")
if likes_python.lower() == "có":
    print("🎉 Tuyệt vời! Python sẽ giúp bạn rất nhiều!")
else:
    print("😊 Không sao, có thể bạn sẽ thích sau!")

# Cách 2: Chuyển thành boolean
has_girlfriend = input("Bạn có bạn gái/trai không? (y/n): ").lower()
is_in_relationship = has_girlfriend in ['y', 'yes', 'có', 'có chứ']
print(f"Tình trạng: {'Đã có người yêu' if is_in_relationship else 'Độc thân'}")

#Nhận Đúng/Sai_Boolean


# Cách 1: Sử dụng try-except (Khuyến nghị)
def input_age():
    while True:
        try:
            age = int(input("Nhập tuổi của bạn: "))
            if age < 0:
                print("❌ Tuổi không thể âm! Thử lại.")
                continue
            elif age > 150:
                print("❌ Tuổi quá lớn! Thử lại.")
                continue
            return age
        except ValueError:
            print("❌ Vui lòng nhập số nguyên! Thử lại.")

# Sử dụng
age = input_age()
print(f"✅ Tuổi hợp lệ: {age}")

#Kiêmtr tra số hợp lệ

def input_name():
    while True:
        name = input("Nhập tên của bạn: ").strip()
        
        if not name:  # Kiểm tra rỗng
            print("❌ Tên không được để trống!")
            continue
        
        if len(name) < 2:
            print("❌ Tên phải có ít nhất 2 ký tự!")
            continue
            
        if not name.replace(" ", "").isalpha():
            print("❌ Tên chỉ được chứa chữ cái!")
            continue
            
        return name.title()  # Viết hoa chữ cái đầu

# Sử dụng
name = input_name()
print(f"✅ Tên hợp lệ: {name}")

#Kiểm tra Text hợp lệ


import re

def input_email():
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    while True:
        email = input("Nhập email: ").strip().lower()
        
        if not email:
            print("❌ Email không được để trống!")
            continue
            
        if re.match(pattern, email):
            return email
        else:
            print("❌ Email không hợp lệ! (vd: ten@gmail.com)")

# Sử dụng
email = input_email()
print(f"✅ Email hợp lệ: {email}")

#Kiểm tra Email hợp lệ
