import qrcode

def generate_qr_code(url):

	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_H,
		box_size=10,
		border=4,
	)

	qr.add_data(url)
	qr.make(fit=True)

	qr_text = qr.print_ascii(invert=True)

	return qr_text