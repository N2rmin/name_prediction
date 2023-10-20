FROM python:3.9
WORKDIR /FrontEnd
COPY ./requirements.txt /FrontEnd/requirements.txt
RUN pip install --no-cache-dir -r /FrontEnd/requirements.txt
COPY ./app /FrontEnd/app
CMD ["streamlit", "run", "app/app.py", "--server.port", "8501"]