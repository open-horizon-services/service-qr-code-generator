from flask import Flask
from flask_restful import Api, Resource,reqparse,abort
from qrcodegen import QrCode, QrSegment
app = Flask("__name__")
api = Api(app)

WEB_SERVER_BIND_ADDRESS = '0.0.0.0'
WEB_SERVER_PORT = 8000
qr_codes = dict()
def to_svg_str(qr: QrCode, border: int) -> str:
	"""Returns a string of SVG code for an image depicting the given QR Code, with the given number
	of border modules. The string always uses Unix newlines (\n), regardless of the platform."""
	if border < 0:
		raise ValueError("Border must be non-negative")
	parts: list[str] = []
	for y in range(qr.get_size()):
		for x in range(qr.get_size()):
			if qr.get_module(x, y):
				parts.append(f"M{x+border},{y+border}h1v1h-1z")
	return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
	<rect width="100%" height="100%" fill="#FFFFFF"/>
	<path d="{" ".join(parts)}" fill="#000000"/>
</svg>
"""
class QR_Code(Resource):
    
    def get(self,name):
        if name not in qr_codes:
            abort(404,message= "QR Code not found")
        return qr_codes[name]
    def post(self, name):
        if name in qr_codes:
            abort(409, message="QR_Code already exists")
        errcorlvl = QrCode.Ecc.LOW  # Error correction level
        qr_code = QrCode.encode_text(name,errcorlvl)
        qr_codes[name] = {"image":to_svg_str(qr_code,4)}
        return "QR_Code has been posted"
    
api.add_resource(QR_Code,"/QR_Code/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)



