FROM python:3.10-alpine

# Update pip to use latest version
RUN pip3 install --upgrade pip
 
COPY ./qr_code_generator /qr_code_generator
WORKDIR /qr_code_generator 
RUN python setup.py install


CMD ["python3","qrcodegen.py"]



