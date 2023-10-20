import uvicorn
from fastapi import FastAPI
from pydantic.main import BaseModel
from model.model import predict_language

# SVM_model = joblib.load(open('C:\\Users\\tn2mi\\Deep Learning\\Learn\\DeploymentFastApi\\app\\model\\SVM_model_language_identifier.pkl', 'rb'))
# SVM_vectorizer = joblib.load(open("C:\\Users\\tn2mi\\Deep Learning\\Learn\\DeploymentFastApi\\app\\model\\SVM_vectorizer.pk","rb"))





app=FastAPI(title="My ML App")

@app.get('/')
def home():
    return "Api is working as expected"

class MyData(BaseModel):
    Name:str

@app.post('/predict')
def predict(data:MyData):
    return predict_language(data.Name)

if __name__ =="__main__":
    uvicorn.run(app, host="0.0.0.0",port=8042)