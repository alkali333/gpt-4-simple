from functions import get_answer, reset_chat
from streamlit_chat import message
import streamlit as st


if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form("ask"):
    question = st.text_area("Ask your question")
    submitted = st.form_submit_button("Go")

# question = "A patient is complaining that his mother is not being allowed to visit him. The staff are saying she will make his mental health deteriorate, he disagrees. What are his rights?"

if question and submitted:
    with st.spinner("Please wait..."):
        if st.session_state.thread_id == None:
            answer, thread_id = get_answer(question)
            st.session_state.thread_id = thread_id
        else:
            answer, _ = get_answer(question, st.session_state.thread_id)

    st.session_state.messages.append(question)
    st.session_state.messages.append(answer)
    # st.write(answer)

    for i, m in enumerate(st.session_state.messages):
        message(m, is_user=i % 2 == 0, key=i)

    st.button("Clear Chat", on_click=reset_chat)
