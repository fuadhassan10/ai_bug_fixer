from google import genai
import streamlit as st
import os,io
from dotenv import load_dotenv

#load the env variable

load_dotenv()

api_key=os.getenv("gemini_api_key")

#initializig a client

client=genai.Client(api_key=api_key)

def ans_generator(images,text):
    prompt=text
    response=client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[images,prompt]
    )
    return response.text