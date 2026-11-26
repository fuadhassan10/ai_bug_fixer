from google import genai
import streamlit as st
import os
import io
from PIL import Image
import time
from api_calling import ans_generator
st.title("_Code_ _Hospital_", anchor=False, text_alignment="center")
st.header("Give me your bugs,I will fix them",text_alignment="center")
# with st.sidebar:
#     with st.container(border=True):
#         st.header("enter your bugs")
#         images = st.file_uploader(
#             "enter your :red[bugs]", ["jpg", "jpeg", "HEIC"], accept_multiple_files=True
#         )
#         pil_image = []

#         for img in images:
#             pil_img = Image.open(img)
#             pil_image.append(pil_img)

#         if pil_image:
#             col = st.columns(len(pil_image))
#         for i, imge in enumerate(pil_image):
#             with col[i]:
#                 st.image(img)

prompt=st.chat_input("what you WANT..",accept_file="multiple",file_type=["jpg","jpeg","heic"])

if prompt:
    texts=prompt.text
    imagess=prompt.files
    # st.image(imagess)
    # st.write(text)
    pil_image = []
    for img in imagess:
        pil_img = Image.open(img)
        pil_image.append(pil_img)
    
    if pil_image:
        col = st.columns(len(pil_image))
    for i, imge in enumerate(pil_image):
        with col[i]:
            st.image(img)
    with st.spinner("AI is generating your answer,please wait",show_time=True):
        ans=ans_generator(pil_image,texts)
        st.markdown(ans)
