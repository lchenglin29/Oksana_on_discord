from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/',methods=['GET'])
def main():
#  print("被監測到了喔")
	return '嗚呼我上線囉'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()