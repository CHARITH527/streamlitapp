import streamlit as st
from forms.contact import contact_form
@st.dialog("Contact Me")
def show_contact_form():
  contact_form()
col1,col2= st.columns(2,gap="small",vertical_alignment="center")
with col1:
    st.image("./Assets/IMG_8861.jpg")
with col2:
    st.title("Charith",anchor=False)
    st.write("Student at GNITC")
    if st.button("Contact Me"):
        show_contact_form()
