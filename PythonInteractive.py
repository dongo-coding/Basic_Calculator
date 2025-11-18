def display_menu():
    print("\n🎯 MENU CHÍNH")
    print("=" * 30)
    print("1. 📊 Tính BMI")
    print("2. 🎲 Chơi game đoán số")
    print("3. 📝 Ghi chú cá nhân")
    print("4. ❌ Thoát")
    print("=" * 30)

def select_menu():
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("❌ Lựa chọn không hợp lệ! Vui lòng chọn 1-4.")

# Sử dụng
while True:
    selection = select_menu()
    
    if selection == 1:
        print("🔄 Đang tính BMI...")
    elif selection == 2:
        print("🎲 Bắt đầu game...")
    elif selection == 3:
        print("📝 Mở ghi chú...")
    elif selection == 4:
        print("👋 Tạm biệt!")
        break
#Menu lựa chọn


import random

def chatbot():
    print("🤖 Xin chào! Tôi là Python Bot!")
    print("💬 Hãy nói chuyện với tôi (gõ 'bye' để thoát)")
    
    responses = {
        "xin chào": ["Xin chào bạn! 😊", "Chào bạn nhé! 👋", "Hello! 🌟"],
        "tên": ["Tôi là Python Bot! 🤖", "Tôi tên là Bot, còn bạn?", "Bot là tên tôi!"],
        "tuổi": ["Tôi vừa được tạo ra! 🆕", "Tôi còn rất trẻ!", "Tuổi? Tôi là AI mà! 😄"],
        "python": ["Python tuyệt vời! 🐍", "Tôi yêu Python!", "Python là ngôn ngữ tốt nhất!"],
        "bye": ["Tạm biệt! 👋", "Bye bye! 🌟", "Hẹn gặp lại! 😊"]
    }
    
    while True:
        user_input = input("\n👤 Bạn: ").lower().strip()
        
        if user_input == "bye":
            print(f"🤖 Bot: {random.choice(responses['bye'])}")
            break
        
        # Tìm từ khóa trong input
        found = False
        for keyword, reply_list in responses.items():
            if keyword in user_input:
                print(f"🤖 Bot: {random.choice(reply_list)}")
                found = True
                break
        
        if not found:
            default_replies = [
                "Thú vị quá! Kể thêm đi! 🤔",
                "Tôi chưa hiểu lắm... 😅",
                "Wow, điều đó thật tuyệt! 🎉",
                "Hm, bạn có thể nói rõ hơn không? 🤷‍♂️"
            ]
            print(f"🤖 Bot: {random.choice(default_replies)}")

# Chạy chatbot
chatbot()

#Chatbot đơn giản
