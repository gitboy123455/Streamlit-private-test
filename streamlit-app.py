import streamlit as web
web.title("This is a test of streamlit!")
web.header("This is a header!")
web.subheader("This is a subheader!")
if web.checkbox("Show/Hide"):
  web.text("Checked")
else:
  web.text("Not checked")
  
