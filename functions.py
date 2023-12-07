from dotenv import load_dotenv
import streamlit as st
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import re

load_dotenv()


def reset_chat():
    st.session_state.thread_id = None
    st.session_state.messages = []


def get_answer(question: str, thread_id: str = "") -> str:
    """This function sends a question to the OpenAI assistant. If a thread ID is specified
    it will continue the thread, otherwise it will start a new thread. In either case it
    will return the answer and the thread id."""

    assistant = OpenAIAssistantRunnable(
        assistant_id="asst_8HFshA1tzFfosxA6G7kzqpCt", as_agent=True
    )

    config_dict = {"content": question}

    if thread_id:
        config_dict["thread_id"] = thread_id

    response = assistant.invoke(config_dict)

    return_values = response.return_values

    return return_values["output"], return_values["thread_id"]
