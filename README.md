# Movie Information Extractor using LangChain and Mistral

## Overview
This project is a simple AI-powered application that extracts structured movie information from unstructured text (paragraphs). It uses LangChain, Mistral AI, and Pydantic to ensure that the output follows a strict and validated JSON format.

The application takes a movie description as input and returns key details such as title, release year, genre, director, cast, rating, and summary.

---

## Features
- Extracts structured data from raw movie descriptions
- Uses a Pydantic model to enforce schema validation
- Ensures consistent and clean output format
- Simple Streamlit user interface for interaction
- Powered by Mistral language model via LangChain

---

## Tech Stack
- Python
- LangChain
- Mistral AI (via `langchain_mistralai`)
- Pydantic
- Streamlit
- python-dotenv

---

## Project Structure
project/
│── app.py # Streamlit UI
│── json-format.py # Core extraction logic (CLI version)
│── .env # API keys
│── README.md


---

## How It Works
1. User provides a movie description.
2. A LangChain ChatPromptTemplate formats the input.
3. The Mistral model processes the prompt.
4. The PydanticOutputParser enforces structured output.
5. The result is displayed in the UI or CLI.

---

## Limitations
- Output quality depends on the input paragraph
- Missing fields may return null or "Not mentioned"
- Model may occasionally generate invalid JSON if prompt is not strictly followed

---

## Future Improvements
- Direct parsing into Pydantic object instead of raw text output
- Improved error handling and retries
- Support for multiple paragraphs (batch processing)
- Export results as JSON file

---

## License
This project is for educational purposes.
