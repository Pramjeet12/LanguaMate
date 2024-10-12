import streamlit as st
import pickle



vector=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))


st.title("Language Detection")
st.write("Enter text to identify.")
user=st.text_area("Enter the text", height=100)

ok = st.button("Predict Language")
if ok:
    user = [user]
    user = vector.transform(user)
    prediction = model.predict(user)
    if prediction == [0]:
       st.subheader("Arabic")
    elif prediction == [1]:
        st.subheader("Chinese")
    elif prediction == [2]:
        st.subheader("Dutch")
    elif prediction == [3]:
        st.subheader("English")
    elif prediction == [4]:
        st.subheader("Estonian")
    elif prediction == [5]:
        st.subheader("French")
    elif prediction == [6]:
        st.subheader("Hindi")
    elif prediction == [7]:
        st.subheader("Indonesian")
    elif prediction == [8]:
        st.subheader("Japanese")
    elif prediction == [9]:
        st.subheader("Korean")
    elif prediction == [10]:
        st.subheader("Latin")
    elif prediction == [11]:
        st.subheader("Persian")
    elif prediction == [12]:
        st.subheader("Portugese")
    elif prediction == [13]:
        st.subheader("Pushto")
    elif prediction == [14]:
        st.subheader("Romanian")
    elif prediction == [15]:
        st.subheader("Russian")
    elif prediction == [16]:
        st.subheader("Spanish")
    elif prediction == [17]:
        st.subheader("Swedish")
    elif prediction == [18]:
        st.subheader("Tamil")
    elif prediction == [19]:
        st.subheader("Thai")
    elif prediction == [20]:
        st.subheader("Turkish")
    elif prediction == [21]:
        st.subheader("Urdu")

