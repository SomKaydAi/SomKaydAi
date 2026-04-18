import streamlit as st
from core_engine import *
from nlp_pipeline import *
from utils import *

st.title("SomKaydAI Chatbot 🤖")
st.write("Ku qor fariintaada hoose:")

engine = SomKaydAI()

user_input = st.text_input("You:")

if user_input:
    if user_input == "exit":
        st.write("Goodbye!")
    elif not is_valid(user_input):
        st.write("Invalid input, try again.")
    else:
        response = engine.process(user_input)
        st.write("SomKaydAI:", response)
