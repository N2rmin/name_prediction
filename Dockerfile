FROM python:3

WORKDIR /NamePrediction

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install pandas
# RUN pip install numpy
# RUN pip install fastapi
# RUN pip install uvicorn
# RUN pip install streamlit
# scikit-learn>=1.3.0
