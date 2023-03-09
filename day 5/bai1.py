
#            0       1       2        3       4       5       6
#           -7      -6      -5       -4      -3      -2      -1
friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
# Lấy ra 4 người bạn đầu tiên trong friends
fist_friends_04 = friends[0:4]
print(fist_friends_04)

# Lấy ra 4 người bạn cuối trong friends
end_friends_04 = friends[3:]
print(end_friends_04)

# Đảo ngược danh sách friends
rv_friends = friends[::-1]
print(rv_friends)

# Lấy ra những người bạn từ vị trí 1 đến hết
print(friends[1:])

# Copy danh sách ban đầu thành một danh sách mới
friends_copy = friends.copy()
print(id(friends_copy), friends_copy)
print(id(friends), friends)

# Lấy ra những người bạn từ vị trí 2 đến sát cuối

two_friendslast = friends[-3:-1]
print(two_friendslast)
