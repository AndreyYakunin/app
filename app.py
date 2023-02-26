import os
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    r = requests.get("https://api.ipify.org?format-json")
    ip = r.json().get("ip")
    my_ip = os.environ.get("IP")
    if ip == my_ip:
        return dict(ip="***.***.***.***")
    return dict(ip=ip)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)