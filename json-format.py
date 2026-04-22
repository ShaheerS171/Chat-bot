from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
model = ChatMistralAI(model_name = "mistral-small-2506")


# now we will create the pydantic model that will take the proper json format from the response
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object= Movie) # this will check if all the things are correct or not

# ====================================================================================================================
# Now in this prompt we will use the model we have make to see the validation
# in the system part we have tell the ai what to do and place the place holder that will tell the ai what to extract
# in the human section we have simply taken the paragraph from the human
# =====================================================================================================================

prompt = ChatPromptTemplate.from_messages(
  ([
    
    ('system', """
    Extract the movie info from the paragraph
     {format_instruction}
"""),
('human', """{paragraph}""")
])
)

#======================================================================================================================
# Now we will take the input from the user store it into the para and then we will use the human template place holder
# we will use the dictionary to give the ipnut of the user to store it into the variable 
# we will use the invoke to fill the place holder
# now we also have to give the format instruction to the system so our system can have the instructions what to extract
#======================================================================================================================

para = input("Give your paragraph: ")
final_prompt = prompt.invoke(
  {"paragraph": para, 
   "format_instruction": parser.get_format_instructions()}
) 


response = model.invoke(final_prompt)
print("==================Bot response=====================")
print(response.content)
