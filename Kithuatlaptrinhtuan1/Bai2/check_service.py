import argparse
import socket

def check_service(host, port):
    try:
        # Tao  TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Dat thoi gian cho thanh 1 giay
        s.settimeout(1)
        # Ket noi voi host va port duoc truyen vao 
        s.connect((host, port))
	# Neu ket noi dc thi in ra dich vu dang running 
        print("Service is running on %s:%s" % (host, port))
    #neu khong ket noi duoc thi in ra dich vu khong hoat dong
    #Neu ket noi bi loi thi in ra dich vu khong hoat dong
    except socket.timeout:
        print("Service is not running on %s:%s" % (host, port))
    except ConnectionRefusedError:
        print("Service is not running on %s:%s" % (host, port))
    except OSError as e:
        print("Error: %s" % e)
    finally:
        s.close()
#Su dung thu vien argarse tao cac tham so lay du lieu tu cmd
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--host", help="host to check")
group.add_argument("--ip-file", help="file containing IP addresses to check")
parser.add_argument("--port", help="port to check", type=int)
parser.add_argument("--port-file", help="file containing ports to check")
args = parser.parse_args()
#Su ly cac truong hop la doi so nao dang duoc su dung
if args.host:
    hosts = [args.host]
    ports = [args.port]
else:
    #Neu la file thi doc roi cho vao mang
    with open(args.ip_file) as f:
        hosts = [line.strip() for line in f]
    with open(args.port_file) as f:
        ports = [int(line.strip()) for line in f]

for host in hosts:
    for port in ports:
        check_service(host, port)
