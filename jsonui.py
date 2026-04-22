import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatMistralAI(model_name="mistral-small-2506")

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ('system', """
    Extract the movie info from the paragraph
     {format_instruction}
"""),
    ('human', """{paragraph}""")
])

st.title("Movie Info Extractor (Pydantic Parser)")

para = st.text_area("Enter Movie Paragraph")

if st.button("Extract"):
    final_prompt = prompt.invoke({
        "paragraph": para,
        "format_instruction": parser.get_format_instructions()
    })

    response = model.invoke(final_prompt)

    st.write("==================Bot response=====================")
    st.write(response.content)