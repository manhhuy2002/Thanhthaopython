import dns.resolver
 
hosts = ["oreilly.com", "yahoo.com", "google.com", "microsoft.com", "cnn.com"]

for host in hosts:
    print(host)
    ip = dns.resolver.resolve(host, "MX")  #thay A bằng NS, MX để có các record khác nhau
			#MX là bản ghi chỉ định Server nào quản lý các dịch vụ Email của tên miền đó
    for i in ip:
        print(i)
