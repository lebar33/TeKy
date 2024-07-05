# Nhập số lượng học sinh
num_students = int(input("Nhập số lượng học sinh: "))

# Nhập thông tin và phân loại cho từng học sinh
for i in range(num_students):
    print("Nhập thông tin học sinh thứ " , i + 1, ":")
    name = input("Tên học sinh: ")
    
    # Nhập điểm Toán và kiểm tra điều kiện
    while True:
        math_score = float(input("Điểm Toán: "))
        if 0 <= math_score <= 10:
            break
        else:
            print("Điểm Toán không hợp lệ. Vui lòng nhập lại trong khoảng từ 0 đến 10.")
    
    # Nhập điểm Văn và kiểm tra điều kiện
    while True:
        literature_score = float(input("Điểm Văn: "))
        if 0 <= literature_score <= 10:
            break
        else:
            print("Điểm Văn không hợp lệ. Vui lòng nhập lại trong khoảng từ 0 đến 10.")
    
    # Nhập điểm Anh và kiểm tra điều kiện
    while True:
        english_score = float(input("Điểm Anh: "))
        if 0 <= english_score <= 10:
            break
        else:
            print("Điểm Anh không hợp lệ. Vui lòng nhập lại trong khoảng từ 0 đến 10.")
    
    # Tính điểm trung bình
    avg_score = (math_score + literature_score + english_score) / 3
    
    # Phân loại học sinh
    if avg_score >= 8.0:
        classification = "Giỏi"
    elif avg_score >= 6.5:
        classification = "Khá"
    elif avg_score >= 5.0:
        classification = "Trung bình"
    else:
        classification = "Yếu"
    
    # In kết quả phân loại cho học sinh
    print(f"\nHọc sinh: {name}")
    print(f"Điểm trung bình: {avg_score:.2f}")
    print(f"Xếp loại: {classification}")

print("\nChương trình đã hoàn thành.")
