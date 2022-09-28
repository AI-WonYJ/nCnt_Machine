import requests

files = open("DB_Machine\sample.jpg", "rb")  # 파일을 'rb'방식으로 연다.
upload = {'file': files}  # 딕셔너리 형식으로 파일 설정
res = requests.post('http://127.0.0.1:5000/', files = upload)  # requests.post(url, data = None, json = None, **kwargs)
