import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
  

load_dotenv()

model = ChatMistralAI(model_name="mistral-small-2506")


prompt = ChatPromptTemplate.from_messages([
    ("system", 
     """You are an AI that extracts key details from movie descriptions.

Extract only the required information and keep it concise.
If a detail is missing, return "Not mentioned".
Do NOT add extra explanations."""
    ),
    
    ("human", 
     """Extract the following details from this movie paragraph:

- Movie Title
- Main Characters
- Setting (time/place)
- Plot Summary (max 2 lines)
- Genre
- Tone

Paragraph:
{input_text}
"""
    )
])

st.title("Movie Detail Extractor")

para = st.text_area("Give your paragraph:")

if st.button("Submit"):
    final_prompt = prompt.invoke({"input_text": para})
    response = model.invoke(final_prompt)
    st.write(response.content)