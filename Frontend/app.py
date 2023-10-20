import streamlit as st
import requests

def main():
    st.title('Name Prediction')

    Name=st.text_input('Name')

    if st.button('Predict'):
    
        payload = {"Name":Name}
        response=requests.post("http://backend:8042/predict",json=payload)
      
        st.write(response.text)
    
if __name__ =="__main__":
    main()