import streamlit as st
import pandas as pd

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("📈 Cathie Wood 👩🏻")
st.markdown("##### CEO, ARK Capital")
st.markdown("---")

st.markdown("#### Claims")


@st.cache(ttl=10)
def run_query():
    sheet_name = "sheet_one"
    data = pd.read_csv(f'https://docs.google.com/spreadsheets/d/1CB6Tz8rddA_T4bTjz2iPiHBx-WLHjhPRkk_pUL5Hozg/gviz/tq?tqx=out:csv&sheet={sheet_name}')
    data = data[(data['name'] == "Cathie Wood") & (data['approval_status'] == "Yes")]
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

for _, row in d.iterrows():
    st.markdown(f'> {row["claim"]}')
    st.text(f'Source: {row["source"]}')
    
    claim_col1, claim_col2, claim_col3 = st.columns(3)

    claim_col1.markdown(f'**Timeline**: {row["period"]}')
    claim_col2.markdown(f'**Date**: {row["date"]}')
    claim_col3.markdown(f'**Status**: `{row["status"]}`')
