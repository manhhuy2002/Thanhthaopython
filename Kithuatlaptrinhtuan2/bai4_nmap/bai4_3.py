# module nmap để tương tác với nmap
import nmap
import argparse
#module argparse để tạo một chương trình dòng lệnh cho phép người dùng truyền vào địa chỉ IP của máy chủ và danh sách các cổng mạng cần quét
parser = argparse.ArgumentParser()

parser.add_argument('-host', type=str, required=True)
parser.add_argument('-p','--port',type=str, required=True, help='port with nmap format')

args = parser.parse_args()

_HOST = args.host
_PORT = args.port

# nmap.PortScannerAsync() hỗ trợ scan bất đồng bộ
portScannerAsync = nmap.PortScannerAsync()

# hàm callback_result dùng để callback (gọi tới khi portScannerAsync thực hiện scan xong)
def callback_result(host, scan_result):
  print(host, scan_result)

# loop qua các port và thực hiện scan
for port in _PORT:
  portScannerAsync.scan(hosts=_HOST, ports=_PORT, callback=callback_result)
# các tiến trình scan sẽ thực hiện song song chứ không chờ lần lưọt

# chờ cho tới khi tất cả scaner thực hiện xong
while portScannerAsync.still_scanning():
  print("Scanning >>>")
  portScannerAsync.wait()
