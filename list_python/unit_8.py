dic_number = {
    "one": "Số một",
    "two" : "số hai", 
    "three": "số ba"
}
"""
tên dic = {
    "key_1" : "value_1", 
    "key_2" : "value_2", 
    .................... 
    "key_n" : "value_n"
}
"""

# In giá trị 
# Chú ý: Dic không sử dụng chỉ số index để truy xuất phần tử, sử dụng key để truy xuất giá trị

# Cú pháp:
# <tên dic>[key]
print(dic_number["two"])
# <tên dic>.get(key)
print(dic_number.get("one"))

# Nhận danh sách của keys

print(dic_number.keys())

# In toàn bộ values có trong dic
print(dic_number.values())

# thay đổi value của key
# <tên dic>[key] = new value
dic_number["one"] = "số mười "


print(dic_number)

# Tạo một dic lưu trữ tên tiếng anh của các số từ 1 đến 10 và ý nghĩa của nó 
# In ra key có tên là four
# Kiểm số lượng phần tử trong dic