# Chương trình Quản Lý Thư Viện

# Khởi tạo danh sách sách trong thư viện
library = [
    {"title": "Doraemon", "author": "JK", "genre": "Truyen tranh"},
    {"title": "OOP", "author": "VT", "genre": "IT"},
    {"title": "Algorithm", "author": "VT", "genre": "IT"}
]


# Hàm thêm sách
def add_book():
    title = input("|Nhập tên sách: ")
    author = input("|Nhập tên tác giả: ")
    genre = input("|Nhập thể loại sách: ")
    book = {
        "title": title,
        "author": author,
        "genre": genre
    }
    library.append(book)
    print("(*) Đã thêm sách thành công!")

# Hàm hiển thị danh sách sách
def display_books():
    if not library:
        print("(*) Thư viện trống!")
        return
    print("\n|Danh sách các cuốn sách trong thư viện:")
    print("*" * 80)  # Đường kẻ ngang
    print("| STT   | Tên sách                      | Tác giả             | Thể loại       |")
    print("-" * 80)  # Đường kẻ ngang
    idx = 1
    for book in library:
        print(f"| {idx:<6}| {book['title']:<30}| {book['author']:<20}| {book['genre']:<15}|")
        idx += 1
    print("*" * 80)  # Đường kẻ ngang

# Hàm tìm kiếm sách theo tên, tác giả hoặc thể loại
def search_books():
    search_query = input("|Nhập tên sách, tên tác giả hoặc thể loại để tìm kiếm: ")
    found_books = [book for book in library if search_query.lower() in book['title'].lower() or search_query.lower() in book['author'].lower() or search_query.lower() in book['genre'].lower()]
    
    if not found_books:
        print("(*) Không tìm thấy sách nào!")
    else:
        print("\n|Kết quả tìm kiếm:")
        print("*" * 80)  # Đường kẻ ngang
        print("| STT   | Tên sách                      | Tác giả             | Thể loại       |")
        print("-" * 80)  # Đường kẻ ngang
        idx = 1
        for book in found_books:
            print(f"| {idx:<6}| {book['title']:<30}| {book['author']:<20}| {book['genre']:<15}|")
            idx += 1
        print("*" * 80)  # Đường kẻ ngang

# Hàm xóa sách
def delete_book():
    display_books()
    if not library:
        return
    book_index = int(input("|Nhập số thứ tự của sách cần xóa: ")) - 1
    if 0 <= book_index < len(library):
        removed_book = library.pop(book_index)
        print("(*) Đã xóa sách '" + removed_book['title'] + "' thành công!")
    else:
        print("(!) Số thứ tự không hợp lệ!")

# Hàm sửa sách
def edit_book():
    display_books()
    if not library:
        return
    book_index = int(input("|Nhập số thứ tự của sách cần sửa: ")) - 1
    if 0 <= book_index < len(library):
        print("\n|Thông tin sách cần sửa:")
        print("|Tên sách: " + library[book_index]['title'])
        print("|Tác giả: " + library[book_index]['author'])
        print("|Thể loại: " + library[book_index]['genre'])
        print("\n|Nhập thông tin mới:")
        new_title = input("|Nhập tên sách mới (Enter để bỏ qua): ")
        new_author = input("|Nhập tên tác giả mới (Enter để bỏ qua): ")
        new_genre = input("|Nhập thể loại sách mới (Enter để bỏ qua): ")

        if new_title:
            library[book_index]['title'] = new_title
        if new_author:
            library[book_index]['author'] = new_author
        if new_genre:
            library[book_index]['genre'] = new_genre
            
        print("\n(*) Đã cập nhật thông tin sách thành công!")
    else:
        print("(!) Số thứ tự không hợp lệ!")

# Menu chính của chương trình
def main_menu():
    print("|" + " "*31 + "QUẢN LÝ THƯ VIỆN"+ " "*31 + "|")
    print('*' * 80)
    while True:
        print("\n")
        print('*' * 80)
        print("| 1. Thêm sách" + " "*65 + "|")
        print("| 2. Hiển thị danh sách sách" + " "*51 + "|")
        print("| 3. Tìm kiếm sách" + " "*61 + "|")
        print("| 4. Xóa sách" + " "*66 + "|")
        print("| 5. Sửa sách" + " "*66 + "|")  # Thêm lựa chọn sửa sách vào menu chính
        print("| 6. Thoát chương trình" + " "*56 + "|")
        print('*' * 80)

        choice = input("|=>Chọn chức năng: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            edit_book()  # Gọi hàm sửa sách khi người dùng chọn lựa chọn số 5
        elif choice == '6':
            print("(*) Đã thoát chương trình!")
            break
        else:
            print("(!) Lựa chọn không hợp lệ, vui lòng chọn lại!")


main_menu()
