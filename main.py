import os
from dotenv import load_dotenv
from streamlit_chat import message
import streamlit as st
from langchain.chat_models import ChatOpenAI

from langchain.schema.messages import HumanMessage, SystemMessage, AIMessage

messages = [SystemMessage(content="You're a helpful assistant")]

load_dotenv()

if "OPENAI_API_KEY" not in os.environ:
    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    else:
        raise EnvironmentError(
            "Open AI key not found in environment variables or Streamlit secrets."
        )


st.set_page_config(
    page_title="GPT-4_Turbo",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content="You're a helpful assistant")]


def reset_chat():
    st.session_state.messages = [SystemMessage(content="You're a helpful assistant")]


st.header("GPT-4-Turbo Chatbot")


with st.form("ask", clear_on_submit=True):
    question = st.text_area("Ask your question")

    submitted = st.form_submit_button("Go")


if question and submitted:
    llm = ChatOpenAI(model_name="gpt-4-1106-preview", temperature=0.5)

    st.session_state.messages.append(HumanMessage(content=question))

    with st.spinner("Please wait..."):
        answer = llm.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=answer.content))

    for i, m in enumerate(st.session_state.messages[1:], start=1):
        message(m.content, is_user=i % 2 != 0, key=i)

    st.button("Clear Chat", on_click=reset_chat)
