def add(a,b):
  return a+b

def substract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  if b==0:
    raise ValueError("Không thể chia cho 0!")
  return a/b

def power(a,b):
  return a**b

def square_root(a):
  if (a<0):
    raise ValueError("Không thể tính căn bậc hai của số âm")
  return a**0.5

  #Các hàm tính toán cơ bản của máy tính

def validate_number(num_str):
  try:
    return float(num_str)
  except ValueError:
    raise ValueError(f"{num_str} không phải là một số hợp lệ") #Hàm kiểm tra đầu vào hợp lệ
  
def validate_operation(operation):
  valid_operations = ['+', '-', '*', '/', '**', 'sqrt']
  if operation not in valid_operations:
    raise ValueError(f"Phép tính {operation} không được hỗ trợ")
  return True

def basic_Calculator():
    print("🧮 MÁY TÍNH CƠ BẢN")
    print("=" * 40)
    print("Các phép tính: +, -, *, /, **, sqrt")
    print("Ví dụ: 5 + 3, 10 / 2, 2 ** 3, sqrt 16")
    print("Gõ 'quit' để thoát")
    print("-" * 40)

    history = []

    while True:
      expression = input("Nhập phép tính: ").strip()
      if expression.lower()=='quit':
        print("👋 Tạm biệt!")        
        display_history(history)
        break

      if expression.lower()=='history':
        display_history(history)
        continue

      if expression.startswith('sqrt'):
        parts = expression.split()
        if len(parts)!=2:
          print("❌ Định dạng: sqrt số")
          continue

        number = validate_number(parts[1])
        res = square_root(number)
        print(f"📊 √{number} = {res}")

        history.append(f"√{number} = {res}")
        continue

      parts = expression.split()
      if len(parts)!=3:
        print("❌ Định dạng: Sai định dạng phép tính")
        continue

      a = validate_number(parts[0])
      operation = parts[1]
      b = validate_number(parts[2])

      if operation == '+':
        res = add(a,b)

      elif operation == '-':
        res = substract(a,b)

      elif operation == '*':
        res = multiply(a,b)

      elif operation == '/':
        res = divide(a,b)

      elif operation == '**':
        res = power(a,b)

      print(f"📊 {expression} = {res}")

      history.append(f"{expression} = {res}")
  

def display_history(history):
  if not history:
    print("📝 Chưa thực hiện bài toán nào")
    return
  
  print("\n📝 LỊCH SỬ TÍNH TOÁN")
  print("=" * 30)

  for i, calc in enumerate(history,1):
    print(f"{i:2d}. {calc}")


def advanced_Calculator():
  print("🚀 MÁY TÍNH NÂNG CAO")
  print("=" * 50)
  print("Tính năng:")
  print("• Phép tính cơ bản: +, -, *, /, **")
  print("• Căn bậc hai: sqrt")
  print("• Tính phần trăm: 50% của 200")
  print("• Tính BMI: bmi 60 1.7")
  print("• Tính lãi suất: lai 1000000 0.05 3")
  print("• Lịch sử: history")
  print("• Thoát: quit")
  print("-" * 50)

  history = []

  while True:
      expression = input("Nhập phép tính: ").strip()
      if expression.lower()=='quit':
        print("👋 Tạm biệt!")        
        display_history(history)
        break

      if expression.lower()=='history':
        display_history(history)
        continue

      if expression.startswith('bmi'):
        res = process_bmi(expression)
        if res:
          history.append(res)
        continue
      if expression.startswith('lai'):
        res = process_interest(expression)
        if res:
          history.append(res)
        continue

      if '%' in expression:
        res = process_percentage(expression)
        if res:
          history.append(res)
        continue

      if expression.startswith('sqrt'):
        parts = expression.split()
        if len(parts)!=2:
          print("❌ Định dạng: sqrt số")
          continue

        number = validate_number(parts[1])
        res = square_root(number)
        print(f"📊 √{number} = {res}")

        history.append(f"√{number} = {res}")
        continue

      parts = expression.split()
      if len(parts)!=3:
        print("❌ Định dạng sai")
        continue

      a = validate_number(parts[0])
      operation = parts[1]
      b = validate_number(parts[2])

      if operation == '+':
        res = add(a,b)

      elif operation == '-':
        res = substract(a,b)

      elif operation == '*':
        res = multiply(a,b)

      elif operation == '/':
        res = divide(a,b)

      elif operation == '**':
        res = power(a,b)

      print(f"📊 {expression} = {res}")

      history.append(f"{expression} = {res}")

def process_bmi(expression):
  parts = expression.split()
  if len(parts)!=3:
    print("❌ Định dạng tính BMI sai")
    return None
  
  w = validate_number(parts[1])
  h = validate_number(parts[2])
  bmi = w/(h**2)

  if bmi < 18.5:
        evaluation = "Thiếu cân"
  elif bmi < 25:
        evaluation = "Bình thường"
  elif bmi < 30:
        evaluation = "Thừa cân"
  else:
        evaluation = "Béo phì"
    
  result = f"BMI: {bmi:.1f} ({evaluation})"
  print(f"📊 {result}")
  return result

def process_interest(expression):
  parts = expression.splti()
  if len(parts) != 4:
    print("❌ Định dạng tính lãi suất sai")
    return None
  

  principal = validate_number(parts[1])
  interest_rate = validate_number(parts[2])
  years = validate_number(parts[3])
    
  final_amount = principal * (1 + interest_rate) ** years
  interest_earned = final_amount - principal
    
  result = f"Lãi suất: {principal:,.0f} → {final_amount:,.0f} (+{interest_earned:,.0f})"
  print(f"📊 {result}")
  return result

def process_percentage(expression):
  if 'của' not in expression:
    print("❌ Định dạng: X% của Y")
    return None
  
  percentage_str, num_str = expression.split('của')
  percentage_str = percentage_str.strip()
  num_str = num_str.strip() #Tách phần trăm và số

  percentage = validate_number(percentage_str.replace('%', ''))
  number = validate_number(num_str) #Lấy số phần trăm

  calc_res = (percentage / 100) * number
    
  res = f"{percentage}% của {number} = {calc_res}"
  print(f"📊 {res}")
  return res

def main_menu():
    while True:
        print("\n🎯 CHƯƠNG TRÌNH MÁY TÍNH PYTHON")
        print("=" * 40)
        print("1. 🧮 Máy tính cơ bản")
        print("2. 🚀 Máy tính nâng cao")
        print("3. 📚 Hướng dẫn sử dụng")
        print("4. 👋 Thoát")
        print("-" * 40)
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == '1':
            basic_Calculator()
        elif choice == '2':
            advanced_Calculator()
        elif choice == '3':
            display_guide()
        elif choice == '4':
            print("👋 Cảm ơn bạn đã sử dụng!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

def display_guide():
    """Hiển thị hướng dẫn sử dụng"""
    print("\n📚 HƯỚNG DẪN SỬ DỤNG")
    print("=" * 50)
    
    print("\n🧮 MÁY TÍNH CƠ BẢN:")
    print("• Cộng: 5 + 3")
    print("• Trừ: 10 - 4")
    print("• Nhân: 6 * 7")
    print("• Chia: 15 / 3")
    print("• Lũy thừa: 2 ** 3")
    print("• Căn bậc hai: sqrt 16")
    
    print("\n🚀 MÁY TÍNH NÂNG CAO:")
    print("• Tất cả phép tính cơ bản")
    print("• Tính BMI: bmi 60 1.7")
    print("• Tính lãi suất: lai 1000000 0.05 3")
    print("• Tính phần trăm: 25% của 200")
    print("• Xem lịch sử: history")
    
    print("\n⚠️  LƯU Ý:")
    print("• Nhập 'quit' để thoát")
    print("• Nhập 'history' để xem lịch sử")
    print("• Sử dụng dấu chấm cho số thập phân")
    print("• Không thể chia cho 0")
    
    input("\nNhấn Enter để quay lại menu chính...")

# 🧮 MÁY TÍNH PYTHON HOÀN CHỈNH
# Tái bản : Đô Ngô
# Ngày: 19/11/2025

def main():
    print("🎉 CHÀO MỪNG ĐẾN VỚI MÁY TÍNH PYTHON!")
    print("🐍 Được sưu tầm bởi Đô Ngô")
    print("=" * 50)
    
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Chương trình bị dừng bởi người dùng!")
    except Exception as e:
        print(f"\n❌ Lỗi không mong muốn: {e}")
    finally:
        print("🔚 Chương trình kết thúc!")

# Chạy chương trình
if __name__ == "__main__":
    main()
  


  
  








      




    


  


  













  
  

