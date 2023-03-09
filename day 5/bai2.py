
students = [["SV001", "Bob", 23], [
    "SV002", "Kenny", 34], ["SV003", "Henry", 45]]
# Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
id_list = 0
id_std = students[id_list][0]
name_std = students[id_list][1]
age_std = students[id_list][2]
print(f"ID: {id_std}, name: {name_std}, age: {age_std}")

# Lấy ra tuổi của sinh viên thứ hai
id_list = 1
print(f"age của sinh viên thứ 2: {age_std}")

# Lấy ra thông tin hai sinh viên cuối cùng

# SV thứ 2
id_std = students[1][0]
name_std = students[1][1]
age_std = students[1][2]
print(f"Thông tin SV 2 ID: {id_std}, name: {name_std}, age: {age_std}")
# SV thứ 3
id_std = students[2][0]
name_std = students[2][1]
age_std = students[2][2]
print(f"Thông tin SV 3 ID: {id_std}, name: {name_std}, age: {age_std}")

# d. Lấy ra id của sinh viên thứ ba
print(f"ID SV 3: {students[2][0]}")
