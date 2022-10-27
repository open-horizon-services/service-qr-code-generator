FROM python:3.10-alpine

# Update pip to use latest version
WORKDIR /qr_code_generator
RUN pip3 install --upgrade pip

RUN pip3 install 
COPY ./ setup.py / 
RUN python setup.py install

COPY ./ qrcodegen.py /

CMD ["python3" "qrcodegen.py"]


