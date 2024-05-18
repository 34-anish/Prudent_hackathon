import streamlit as st
import pickle
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
model=pickle.load(open('unsupervised_model.pkl','rb'))

def predict_model(input):
        vectorizer = TfidfVectorizer()
        X_train_tfidf = vectorizer.fit_transform(input)
        return model.predict(X_train_tfidf)



def main():
    st.title("Sentiment Analysis on Customer Reviews")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Sentiment Analyzer </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    input = st.text_input("Review Demo","Type your review here to check the sentiment")
    if st.button("Predict"):
        output = predict_model([input])
        if output == 1:
            st.markdown("<h2 style='color:green;text-align:center;'>Sentiment: Positive</h2>", unsafe_allow_html=True)
        elif output == 0:
            st.markdown("<h2 style='color:blue;text-align:center;'>Sentiment: Neutral</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color:red;text-align:center;'>Sentiment: Negative</h2>", unsafe_allow_html=True)


if __name__=='__main__':
    main()