import streamlit as st
import pandas as pd

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("🏦🤑🏦")
st.subheader("Tracking Word of Mouth Global Economy Predictions")
st.markdown("A tool for investors to track global financial sentiment, and keep leaders, fund managers and TikTok influencers accountable for their financial predictions — both good and bad")
st.markdown('---')
st.header("Global Accountability Index")

@st.cache(ttl=10)
def run_query():
    sheet_name = "sheet_one"
    data = pd.read_csv(f'https://docs.google.com/spreadsheets/d/1CB6Tz8rddA_T4bTjz2iPiHBx-WLHjhPRkk_pUL5Hozg/gviz/tq?tqx=out:csv&sheet={sheet_name}')
    data = data[(data['approval_status'] == "Yes")]
    pending_data = data[(data['status'] == "Pending")]
    correct_data = data[(data['status'] == "Correct")]
    incorrect_data = data[(data['status'] == "Incorrect")]
    inconclusive_data = data[(data['status'] == "Inconclusive")]

    return len(pending_data), len(correct_data), len(incorrect_data), len(inconclusive_data), data

pending, correct, incorrect, inconclusive, d = run_query()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Incorrect", incorrect, "0% since last week", delta_color="off")
col2.metric("Correct", correct, "0% since last week", delta_color="off")
col3.metric("Pending", pending, "0% since last week", delta_color="off")
col4.metric("Inconclusive", inconclusive, "0% since last week", delta_color="off")

col1, col2 = st.columns(2)

col1.subheader("Submit a prediction")
col2.subheader("Add a new person")

# st.sidebar.markdown("Finfluencer Accountability")

with col1.form(key='predictions'):
    personality = st.text_input('Who said it?', placeholder="Ken Griffin")
    prediction = st.text_input('Link to what was said (Twitter, Youtube, News)', placeholder="https://finance.yahoo.com/ken-griffin-crypto")
    st.form_submit_button('Submit a prediction')

with col2.form(key='new_finfluencer'):
    new_personality = st.text_input('Who do you want us to track?', placeholder="Tom Brady")
    new_links = st.text_input('Relevant links (optional)', placeholder="https://espn.com/tom-brady")
    st.form_submit_button('Review new person')