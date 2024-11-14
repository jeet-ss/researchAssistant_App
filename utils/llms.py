import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

def instantiate_LLM(
    LLM_provider, api_key, temperature=0.5, top_p=0.95, model_name=None
):
    """Instantiate LLM in Langchain.
    Parameters:
        LLM_provider (str): the LLM provider; in ["OpenAI","Google"]
        model_name (str): in ["gpt-3.5-turbo", "gpt-3.5-turbo-0125", "chatgpt-4o-latest","gemini-pro"].
        api_key (str): google_api_key or openai_api_key
        temperature (float): Range: 0.0 - 1.0; default = 0.5
        top_p (float): : Range: 0.0 - 1.0; default = 1.
    """
    if LLM_provider == "OpenAI":
        llm = ChatOpenAI(
            api_key=api_key,
            model=model_name,
            temperature=temperature,
            top_p=top_p
        )
    if LLM_provider == "Google":
        llm = ChatGoogleGenerativeAI(
            google_api_key=api_key,
            # model="gemini-pro",
            model=model_name,
            temperature=temperature,
            top_p=top_p,
            convert_system_message_to_human=True,
        )

    return llm


def instantiate_LLM_main():
    """Instantiate the selected LLM model."""
    try:
        # Check model and associated keys
        if st.session_state.LLM_provider == "OpenAI" and st.session_state.model_api_key.startswith("sk-"):
            llm = instantiate_LLM(
                "OpenAI",
                api_key=st.session_state.model_api_key,
                temperature=st.session_state.temperature,
                top_p=st.session_state.top_p,
                model_name=st.session_state.selected_model,
            )
        # elif st.session_state.LLM_provider == "Google" and st.session_state.google_api_key != "":
        #     llm = instantiate_LLM(
        #         "Google",
        #         api_key=st.session_state.model_api_key,
        #         temperature=st.session_state.temperature,
        #         top_p=st.session_state.top_p,
        #         model_name=st.session_state.selected_model,
        #     )
        else:
            raise ValueError("Api key is not provided or is incorrect!")
    except Exception as e:
        st.error(f"An error occured: {e}")
        llm = None
    return llm