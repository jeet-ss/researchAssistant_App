import streamlit as st


list_LLM_providers = [":rainbow[**OpenAI**]"]#, "**Google Generative AI**"]

list_WebSearch_providers = [":rainbow[**Tavily**]", "**DuckDuckGo**"]

def expander_model_parameters(
    LLM_provider="OpenAI",
    text_input_API_key=None,
    list_models=["gpt-4o", "gpt-4o-mini", "gpt-4-turbo-preview"],
    openai_api_key="",
    google_api_key="",
):
    """Add a text_input (for the API key) and a streamlit expander with models and parameters."""

    st.session_state.LLM_provider = LLM_provider

    if LLM_provider == "OpenAI":
        st.session_state.model_api_key = st.text_input(
            text_input_API_key,
            value=None,
            type="password",
            placeholder="insert your OPENAI API key",
        )

    # if LLM_provider == "Google":
    #     st.session_state.google_api_key = st.text_input(
    #         text_input_API_key,
    #         type="password",
    #         value=google_api_key,
    #         placeholder="insert your GOOGLE API key",
    #     )

    with st.expander("**Models and parameters**"):
        st.session_state.selected_model = st.selectbox(
            f"Choose {LLM_provider} model", list_models
        )
        # model parameters
        st.session_state.temperature = st.slider(
            "temperature",
            min_value=0.1,
            max_value=1.0,
            value=0.0,
            step=0.1,
        )
        st.session_state.top_p = st.slider(
            "top_p",
            min_value=0.1,
            max_value=1.0,
            value=0.95,
            step=0.05,
        )

def expander_websearch_parameters(
    webSearchTool_provider="Tavily",
    text_input_API_key=None,
    #list_models=["gpt-4o", "gpt-4o-mini", "gpt-4-turbo-preview"],
    tavily_api_key="",
    #google_api_key="",
):
    
    """Add a text_input (for the API key) and a streamlit expander with models and parameters."""


    st.session_state.webSearchTool_provider = webSearchTool_provider

    if webSearchTool_provider == "Tavily":
        st.session_state.webSearchTool_api_key = st.text_input(
            text_input_API_key,
            value=None,
            type="password",
            placeholder="insert your Tavily API key",
        )


    with st.expander("**Parameters**"):
        # model parameters
        st.session_state.max_results = st.slider(
            "Max results to return",
            min_value=2,
            max_value=6,
            value=3,
            step=1,
        )
 
def app_sidebar():
    """Create a SideBar"""
    with st.sidebar:

        st.caption(
            "🚀 An App powered by 🔗 LangGraph"
        )
        st.divider()

        llm_chooser = st.radio(
            "Select LLM provider",
            list_LLM_providers,
            captions=[
                "[OpenAI pricing page](https://openai.com/pricing)",
                "Rate limit: 60 requests per minute.",
            ],
        )

        if llm_chooser == list_LLM_providers[0]:
            expander_model_parameters(
                LLM_provider="OpenAI",
                text_input_API_key="OpenAI API Key - [Get an API key](https://platform.openai.com/account/api-keys)",
                list_models = ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo-preview"],
                #openai_api_key=openai_api_key,
                #api_key=openai_api_key,
            )

        # if llm_chooser == list_LLM_providers[1]:
        #     #google_api_key = st.sidebar.text_input('Google API Key', type='password')
        #     expander_model_parameters(
        #         LLM_provider="Google",
        #         text_input_API_key="Google API Key - [Get an API key](https://makersuite.google.com/app/apikey)",
        #         list_models=["gemini-pro", "gemini-1.5-pro"],
        #         #openai_api_key=openai_api_key,
        #         #api_key=google_api_key,
        #     )

        ####################
        st.divider()

        web_search_tool_chooser = st.radio(
            "Select Web Search Tool provider",
            list_WebSearch_providers,
            captions=[
                '''[Tavily AI API key / Pricing page](https://app.tavily.com/) 
                    Free Limit: 1000 requests per month''',
                "Rate limit: 60 requests per minute.",
            ],
        )

        if web_search_tool_chooser == list_WebSearch_providers[0]:
            expander_websearch_parameters(
                webSearchTool_provider="Tavily",
                text_input_API_key="Tavily API Key - [Get an API key](https://platform.openai.com/account/api-keys)",
                #list_models = ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo-preview"],
                #tavily_api_key = 
                #openai_api_key=openai_api_key,
                #api_key=openai_api_key,
            )
        
        elif web_search_tool_chooser == list_WebSearch_providers[1]:
            expander_websearch_parameters(
                webSearchTool_provider="Duck",
                text_input_API_key="Tavily API Key - [Get an API key](https://platform.openai.com/account/api-keys)",
                #list_models = ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo-preview"],
                #tavily_api_key = 
                #openai_api_key=openai_api_key,
                #api_key=openai_api_key,
            )
