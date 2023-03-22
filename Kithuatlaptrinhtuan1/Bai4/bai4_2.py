
'''
urllib là một mô-đun của Python có thể dùng để mở các URL. Nó định nghĩa các hàm và lớp giúp thao tác với URL. Với Python, 
bạn cũng có thể truy cập và trích xuất dữ liệu từ internet như XML, HTML, JSON, v.v. 
Bạn cũng có thể sử dụng Python để xử lý trực tiếp các dữ liệu này.
'''

import urllib.request
from urllib.request import Request

# nhập đường dẫn từ URL từ người dùng 
url = input("Enter url: ")   # vd: http://www.google.com

# ở đây đặt sẵn USER_AGENT để gửi yêu cầu
USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36'

# hàm thực hiện sử dujgn user=agent của Chrome
def chrome_user_agent():
    opener = urllib.request.build_opener() # urllib.request.build_openner dùng để mở các URL
    
    # sau đó chúng ta có thể tham user-agent vào các header của opener
    opener.addheaders = [('User-agent', USER_AGENT)]  
    
    # cài đặt opener để có thể sử dụng trên toàn bộ ứng dụng
    urllib.request.install_opener(opener)
    
    # tại đấy chúng ta có thể mwor URL và lấy phản hồi gán vào response
    response = urllib.request.urlopen(url)
    print("Response headers")
    print("------------------")
    
    """
    vòng for này dùng để lấy các thông tin tiêu đề (header) của phản hồi đưuọc trả về.
    Mỗi thông tin được lấy ra và in ra màn hình dưới dạng header:value
    vd: Content-Type:text/html
    """
    # in ra các header của response
    for header,value in response.getheaders():
        print(header + ":" + value)
        
    # sau đó tiếp tục tạo một request với url và user-agent
    request = Request(url)
    request.add_header('User-agent', USER_AGENT)
    print("\nRequest headers")
    print("------------------")
    
    """
    tương tự như response nhưng vòng for này dùng để lấy header của request.
    """
    
    for header, value in request.header_items(): 
        # request.header_item() là phương thức của Request trả về một danh sách các cặp giá trị key:value là thông tin header của Request
        print(header + ":" + value)

if __name__ == '__main__':
    chrome_user_agent()
