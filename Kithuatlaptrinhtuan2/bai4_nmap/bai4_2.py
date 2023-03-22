#!/usr/bin/env python3

# module nmap để tương tác với nmap
import nmap
import argparse
#module argparse để tạo một chương trình dòng lệnh cho phép người dùng truyền vào địa chỉ IP của máy chủ và danh sách các cổng mạng cần quét.
parser = argparse.ArgumentParser()

parser.add_argument('-host', type=str, required=True)
parser.add_argument('-c','--command', type=str, required=False, help='nmap command')
parser.add_argument('-p','--port',type=str, required=True, help='port')

args = parser.parse_args()

_HOST = args.host
_PORT = args.port
_COMMAND = args.command if args.command else ''

class NmapScanner:
  def __init__(self) -> None:
    self.portScanner = nmap.PortScanner()

  # hàm nmapScan thực hiện scan ip, port được đưa vào với command cộng thêm nếu có
  def nmapScan(self, ip, port, command):
    self.portScanner.scan(ip, arguments="-n -p{} {}".format(port, command))
    print("Trying {} : {}".format(ip, port))
    return self.portScanner

scanner = NmapScanner().nmapScan(_HOST, _PORT, _COMMAND)

# host_list lưu các mục tiêu vừa quét
host_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]

for host, status in host_list:
  # loop qua các protocol 
  for protocol in scanner[host].all_protocols():
    print("protocol: {}".format(protocol))
    # listPort lưu các host đã scan
    listPort = scanner[host]['tcp'].keys()
    # loop qua các port đã quét của host, in kết quả
    for port in listPort:
      print("Port {} State : {}".format(port, scanner[host][protocol][port]['state']))
