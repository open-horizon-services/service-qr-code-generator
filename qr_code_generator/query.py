from flask import Flask
from flask import request
import ipaddress

WEB_SERVER_BIND_ADDRESS = '0.0.0.0'
WEB_SERVER_PORT = 8000

ip = None

webapp = Flask('query')

template="""
<!DOCTYPE html>\r\n
<html lang="en">\r\n<head>\r\n
<meta charset=\"utf-8\">\r\n
<title>query</title>\r\n
</head>\r\n<body>\r\nArguments: \"{arguments}\".\r\n \r\n ip = {ipaddr} \r\n</body>\r\n</html>\r\n
"""

@webapp.route("/query", methods=['GET'])
def hello():
    global ip
    parameters = request.args.copy()
    if 'ip' in parameters:
        try:
            ip = ipaddress.ip_address(parameters.get('ip'))
        except ValueError:
            print("Error: Invalid IP Address")

    return template.format(arguments=parameters, ipaddr = ip)

if __name__ == '__main__':
  webapp.run(host=WEB_SERVER_BIND_ADDRESS, port=WEB_SERVER_PORT)