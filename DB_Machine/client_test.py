import requests
files = open("DB_Machine\sample.jpg", "rb")
upload = {'file': files}
res = requests.post('http://127.0.0.1:5000/image/', files = upload)