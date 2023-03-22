import requests

# Replace "example.com" with the domain you want to get information about
url = input("url: ")
response = requests.get(url)

# Get Request module version
request_version = requests.__version__

# Get license information
license_info = requests.__license__

# Get copyright information
copyright_info = requests.__copyright__

# Get author and author email
author_info = requests.__author__
author_email_info = requests.__author_email__

# Lấy document URL, title, and description
document_url = response.url
document_title = response.text.split("<title>")[1].split("</title>")[0]
document_description = response.text.split('<meta name="description" content="')[1].split('"')[0]

print(f"Request module version: {request_version}")
print(f"License information: {license_info}")
print(f"Copyright information: {copyright_info}")
print(f"Author information: {author_info}")
print(f"Author email information: {author_email_info}")
print(f"Document URL: {document_url}")
print(f"Document title: {document_title}")
print(f"Document description: {document_description}")