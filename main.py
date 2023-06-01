from backend import run_llm

import streamlit as st

from streamlit_chat import message

st.header("Технічна підтримка")

query = st.text_input("Питання", placeholder="Введіть Ваше питання")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if query:
    with st.spinner("Відповідаємо.."):
        generated_response = run_llm(query=query, chat_history=st.session_state["chat_history"])

        formatted_response = f"{generated_response['answer']}"

        st.session_state["user_prompt_history"].append(query)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append((query, generated_response["answer"]))

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)
