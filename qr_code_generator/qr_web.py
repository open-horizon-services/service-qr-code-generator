from flask import Flask
from qrcodegen import generate_qr_code

app = Flask(__name__)

@app.route("/")
def get_name():

    return "My Local server!"

if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    qrcode = generate_qr_code(url)
    print(qrcode)
    app.run()