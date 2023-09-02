import os
import time
import requests
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
    return "Your bot is alive!"


def run():
    app.run(host="0.0.0.0", port=8080)


def ping():
    # url = os.environ['SELF_URL']
    url = ''
    res = requests.request("GET", url)
    print(res)
    time.sleep(1)


def keep_alive():
    server = Thread(target=run)
    server.start()
    # monitor = Thread(target=ping)
    # monitor.start()


keep_alive()
