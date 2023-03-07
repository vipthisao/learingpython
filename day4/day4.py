
# 1. Tạo một movies list chứa tên các bộ phim đã xem
move_list = ['halo', 'Doctor_Strange', 'Fast & Furious',
             'Iroman', 'gió', 'halo', 'One Piece', 'Spiderman']
print("list phim ban đầu", move_list)

# # 2. Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
move_list.insert(0, input("Nhập tên phim :"))
print(move_list)

# # 3.Thêm bộ phim vừa nhập vào cuối của danh sách movies
move_insert = move_list[0]
move_list.append(move_insert)
print(move_list)

# # 4.In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
move_giua = len(move_list)//2
print("Phim đầu là: ", move_list[0])
print("Phim giữa là: ", move_list[move_giua])
print("Phim cuối là: ", move_list[-1])

# 5.Tính tổng bộ phim có trong movies
move_number = len(move_list)
print(f"Có {move_number} bộ phim")

# 6.Xóa bộ phim đầu và cuối trong movies
del move_list[0], move_list[-1]
print("list còn lại", move_list)

# 7.Lấy ra và xóa bộ phim cuối cùng trong movies
print(move_list.pop(-1))
print("List còn lại sau khi xóa phim cuối cùng: ", move_list)

# 8.Chèn một bộ phim bất kỳ vào đầu danh sách movies
move_list.insert(0, 'Avatar')
print("Bộ phim được chèn thêm vào:", move_list)

# 9.Đếm số bộ phim có tiêu đề là "One Piece"
move_view = move_list.count("One Piece")
print(f"One Pice xuất hiện {move_view} lần trong list phim")

# 10.Tìm vị trí của bộ phim có tên là "gió"
move_vitri = move_list.index('gió')
print(f"vị trí {move_vitri} là phim gió ")

# 111.Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
move_list.extend(['Đất và người', 'Sinh Tử'])
print(move_list)

# 12.Xóa tất cả các bộ phim có trong danh sách
move_list.clear()
print(move_list)
