import argparse
import socket
import platform

def get_system_info(url):
    try:
        # Lay hostname tu URL
        hostname = socket.gethostbyname(url)
        # Lay dia chi IP tu hostname
        ip_address = socket.gethostbyname(hostname)
        # Lay thong tin ve he dieu hanh
        os = platform.system() + " " + platform.release()
        # Lay thong tin ten may chu
        host_name = socket.gethostname()

        print("URL:", url)
        print("Hostname:", hostname)
        print("IP Address:", ip_address)
        print("Operating System:", os)
        print("Host Name:", host_name)
        print("-" * 40)
    except socket.gaierror:
        print("Could not resolve hostname for URL:", url)
#Su dung thu vien argarse tao cac tham so lay du lieu tu cmd
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL to scan")
parser.add_argument("--url-file", help="file containing URLs to scan")
args = parser.parse_args()

if args.url:
    urls = [args.url]
elif args.url_file:
    ##Neu la file thi doc roi cho vao mang
    with open(args.url_file) as f:
        urls = [line.strip() for line in f]
else:
    print("Please specify a URL using --url or a URL file using --url-file")
    exit()

# Check url duoc truyen vao thong qua vong for
for url in urls:
    get_system_info(url)
