from functions import get_answer, reset_chat
from streamlit_chat import message
import streamlit as st

st.set_page_config(
    page_title="Mental Health Advocate Advisor ChatBot from Alkali Media",
    page_icon="📢",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)


if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("📢 Mental Health Advocate Advisor ChatBot")

st.write(
    """This chatbot provides informations for IMHAs and Community Mental Health Advocates. 
         You can ask about a specific case, request information about mental health legislation, 
         or draft a letter / email. It has been trained to use the Mental Health Act and Code Of Practice. """
)

with st.form("ask", clear_on_submit=True):
    question = st.text_area("Ask your question")

    options = [
        "Choose an option",
        "Informal",
        "Section 2",
        "Section 3",
        "CTO",
        "Section 37",
        "Section 37/41",
    ]

    selected_option = st.selectbox("Patient Status (optional):", options)

    submitted = st.form_submit_button("Go")

# question = "A patient is complaining that his mother is not being allowed to visit him. The staff are saying she will make his mental health deteriorate, he disagrees. What are his rights?"

if question and submitted:
    options_dict = {
        "Choose an option": "",
        "Informal": "The patient is voluntary / informal - not subject to detention",
        "Section 2": "The patient is detained under section 2",
        "Section 3": "The patient is detained under section 3",
        "CTO": "The patient is subject to a community treatment order",
        "Section 37": "The patient is detained under section 37",
        "Section 37/41": "The patient is detained under section 37/41",
    }

    question += f" \n\n {options_dict[selected_option]}"

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

st.write("\n\n\n")
st.write("-" * 888)
st.info(
    body="""
    Disclaimer And Privacy Information:

    Please note that this ChatBot is designed to support Independent Mental Health Advocates by providing information based on the Mental Health Act and the Code of Practice. However, it is not a substitute for professional legal advice. While every effort has been made to ensure the accuracy of the information provided, the ChatBot relies on algorithms that may not capture the nuances of individual cases. Therefore, users are advised to verify any legal references or information provided by the ChatBot before taking action.

    It is important to highlight that this application does not retain any personal data. Nevertheless, as the information is processed through OpenAI's API, we strongly recommend against incorporating any real names or sensitive personal details within your queries. Instead, use placeholders such as initials, and replace them with the actual details after receiving the generated information.

    Always exercise due diligence and consult with your line manager or a legal professional to ensure the appropriateness of the information before employing it in your advocacy work. The creators of this ChatBot and associated parties bear no responsibility for any actions taken based on its usage.
    """
)
