FROM python:3.7
COPY requirements.txt /BackEnd
WORKDIR /BackEnd
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt 
COPY . /BackEnd
EXPOSE 8042
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8042" ]