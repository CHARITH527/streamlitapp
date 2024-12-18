import streamlit as st
st.title("APP")
aboutme=st.Page(
    title="About me",
    page="views/aboutme.py",
   
)
page1=st.Page(
    title="Chatbot",
    page="views/chatbot.py",
   
)

page2=st.Page(
    title="Sales",
    page="views/salesdashboard.py",
   
)

st.logo("Assets/IMG_8861.jpg")
st.sidebar.text("Made with Love By charith")
nav=st.navigation(
    {
        "Info":[aboutme],
        "Projects":[page1,page2],
    }
)
nav.run()