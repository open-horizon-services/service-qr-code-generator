FROM python:3.10-alpine

# Update pip to use latest version
RUN pip3 install --upgrade pip

RUN pip3 install 
COPY ./ qr_code_generator/setup.py / 
RUN python setup.py install

COPY ./ qr_code_generator/qrcodegen.py /

CMD python3 qr_code_generator/qrcodegen.py