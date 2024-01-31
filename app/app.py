import streamlit as st
import re
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load the model
with open('log_model.pkl', 'rb') as file:
    log_model = pickle.load(file)

# Load the vectorizer
with open('count_vectorizer.pkl', 'rb') as file:
    count_vectorizer = pickle.load(file)

def preprocess_email(email):
    # Lowercase the email
    email = email.lower()

    # Remove punctuation
    punctuation_pattern = r'[^\w\s]'
    email = re.sub(punctuation_pattern, '', email)

    # Tokenize the email
    email_tokens = email.split()

    # Remove stop words
    stop_words = set(stopwords.words('french'))
    email_tokens = [token for token in email_tokens if token not in stop_words]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    email_tokens = [lemmatizer.lemmatize(token) for token in email_tokens]

    # Join the tokens back together
    email = ' '.join(email_tokens)

    return email

st.set_page_config(layout='wide', initial_sidebar_state='auto', page_title='Phishing Email Detector', page_icon=None)

st.markdown("<h1 style='text-align: center; color: white;'>Phishing Email Detector</h1>", unsafe_allow_html=True)

st.sidebar.header('Enter the email text')
email = st.sidebar.text_area("Email")

if email:
    # Preprocess the email
    email = preprocess_email(email)

    # Transform the email into a vector of features
    email_vectorized = count_vectorizer.transform([email])

    # Convert the result to an array
    email_array = email_vectorized.toarray()

    # Now you can use your model to predict whether the email is a phishing email or not
    prediction = log_model.predict(email_array)

    if prediction[0] == 1:
        st.markdown("<p style='color:red;'>It is a phishing email man, come on!</p>", unsafe_allow_html=True)
        st.image('phishing.gif')
    else:
        st.success('This email is safe')
