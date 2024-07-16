list_a = [1, 20, 4, 9, 5]
#  Sắp xếp theo thứ tự tăng dần không sử dụng sort()
# Ý tưởng: Tạo một list mới để chứa dãy sau khi đã được sắp xếp
# Tìm giá trị nhỏ nhất có trong list_a sau đó thêm vào list mới, xóa giá trị
# trong list a

list_b = []
# Làm sao để biết list_a không có giá trị trong đó? len(list_b ) == 0


while len(list_a) != 0:
    min_value = min(list_a)
    print("min_value: ", min_value)
    list_b.append(min_value)
    list_a.remove(min_value)

print(list_b)


# min = 1
# list_b = [1]
# list_a = [ 20, 4, 9, 5]

# min = 4
# list_b = [1, 4]
# list_a = [ 20, 9, 5]



