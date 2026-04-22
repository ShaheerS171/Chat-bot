from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model_name = "mistral-small-2506")

#========================================================================================================================
# now this will make the prompt that will make the personality of the system through the system and also it will 
# give the prompt from the human side but there is a place holder{} in the human thing this is where we give our content
# Now the prompt is ready and we just have to give the paragraph and it will summarize this thing
# You have to give it as a list
#========================================================================================================================

prompt = ChatPromptTemplate.from_messages(
  ([
    
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
)

#======================================================================================================================
# Now we will take the input from the user store it into the para and then we will use the human template place holder
# we will use the dictionary to give the ipnut of the user to store it into the variable 
# we will use the invoke to fill the place holder
#======================================================================================================================

para = input("Give your paragraph: ")
final_prompt = prompt.invoke(
  {"input_text": para}
)


response = model.invoke(final_prompt)
print("==================Bot response=====================")
print(response.content)
