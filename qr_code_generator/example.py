import requests
from json import loads
from cairosvg import svg2png

BASE = "http://127.0.0.1:5000/"


requests.post(BASE + "QR_Code/hello")
response = requests.get(BASE+ "QR_Code/hello")
response = response.text

svg2png(bytestring=loads(response)["image"],write_to='output.png')