import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


SVM_model = joblib.load(open(f'{BASE_DIR}/SVM_model_language_identifier.pkl', 'rb'))
SVM_vectorizer = joblib.load(open(f'{BASE_DIR}/SVM_vectorizer.pk',"rb"))
def predict_language(text):
    serie = pd.Series(text)
    vector = SVM_vectorizer.transform(serie)
    return str(SVM_model.predict(vector)[0])