
'''
HTTP client thiết lập một kết nối TCP đến server. Nếu thiết lập thành công, client và 
server sẽ truyền nhận dữ liệu với nhau thông qua kết nối này
'''

import http.client

# Nhập tên miền hoặc địa chỉ IP của máy chủ web
host = input("Enter host: ")

# Tạo đối tượng kết nối HTTP đến máy chủ web
connection = http.client.HTTPConnection(host)

# Gửi yêu cầu GET đến đường dẫn "/"
connection.request("GET", "/")

# Nhận phản hồi từ máy chủ
response = connection.getresponse()

# In kiểu dữ liệu của đối tượng phản hồi (response)
print(type(response))

# In mã trạng thái (status) và thông điệp trạng thái (reason) của phản hồi
print(response.status, response.reason)

# Nếu mã trạng thái của phản hồi là 200 (tức là thành công)
if response.status == 200: 
    # nếu trạng thái là 200 thì đọc dữ liệu phản hồi và in ra màn hình
    data = response.read()
    print(data)
