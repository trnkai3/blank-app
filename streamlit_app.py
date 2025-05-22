import streamlit as st

st.title("🎈 My new app")

st.header("Diva Test")

name = st.text_input("Enter your name")

studymethod = st.selectbox("Study method", ("Crammer", "Memory Box", "Pre-planner"))

button = st.button("Go")

if button:
    with st.spinner("Loading your results"):
        if studymethod == "Crammer":
            st.write(f"{name}, You are NOT a diva")
        elif studymethod == "Pre-planner":
            st.write(f"{name}, You are a diva")
        elif studymethod == "Memory Box":
            st.write(f"{name}, You are almost a diva")

