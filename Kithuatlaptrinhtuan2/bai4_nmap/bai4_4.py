# module os hỗ trợ tương tác với hệ thống
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-c','--command', type=str, required=True, help='nmap command')
args = parser.parse_args()

_COMMAND = args.command

# truyền lệnh vào hàm os.system để chạy nmap
os.system(_COMMAND)

# nmap example.com -Pn -sV -O -v
