import nmap
#tao 1 doi tuong PortScanner de quet cac cong mang                    
portScanner = nmap.PortScanner()
#nhập địa chỉ IP hoặc tên miền của máy chủ cần quét 
host_scan = input('Host scan: ')

portlist="21,22,23,25,80"	

portScanner.scan(hosts=host_scan, arguments='-n -p'+portlist)

print(portScanner.command_line())
#Dòng này tạo danh sách tất cả các máy chủ đã được quét cùng với trạng thái của chúng. 
#Phương thức  all_hosts()trả về danh sách tất cả các máy chủ đã được quét và statustừ điển chứa thông tin về trạng thái của từng máy chủ
hosts_list = [(x, portScanner[x]['status']['state']) for x in portScanner.all_hosts()]

#in trạng thái của từng máy chủ đã được quét.
for host, status in hosts_list:
    print(host, status)
#in thông tin về các cổng mở trên mỗi máy chủ được quét
for protocol in portScanner[host].all_protocols():
    print('Protocol : %s' % protocol)
    listport = portScanner[host]['tcp'].keys()
    for port in listport:
        print('Port : %s State : %s' % (port,portScanner[host][protocol][port]['state']))
