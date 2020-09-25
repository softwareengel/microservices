import http.client
import mimetypes
import xml.etree.ElementTree as ET
from time import sleep

conn = http.client.HTTPConnection("127.0.0.1", 8080)

payload = ""

headers = {
    'Content-Type': 'application/xml'
}

conn.request("GET", "/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

