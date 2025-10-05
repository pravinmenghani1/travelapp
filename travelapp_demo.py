import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-5",api_key=OPENAI_API_KEY)
prompt_template = PromptTemplate(
    input_variables = ["city","month","language","budget"],
    template = """
    Welcome to the {city} travel guide!
    If you're visiting in {month}, here's what you can do:
    1. Must-visit attractions.
    2. Local cuisine you must try.
    3. Useful phrases in {language}.
    4. Tips for traveling on a {budget} budget.
    Enjoy your trip!
    """
)

st.title("Travel App")

city = st.text_input("Enter the city")
month = st.text_input("Enter the month")
language = st.text_input("Enter the language")
budget = st.number_input("Enter the budget")
if city:
    response = llm.invoke(prompt_template.format(city=city,
                                                 month=month,
                                                 language=language,
                                                 budget=budget
                                                 ))
    st.write(response.content)
    print(response)