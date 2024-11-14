import streamlit as st

# Web search tool
from langchain_community.tools.tavily_search import TavilySearchResults

def instantiate_webSearchTool(
    webSearchTool_provider: str, api_key: str, max_results: int
):
    """Instantiate webSearchTool in Langchain.
    Parameters:
        webSearchTool_provider (str): the webSearchTool provider; in ["Tavily"]
        api_key (str): tavily_api_key or ...
        max_results (int): Range: 2 - 6; default = 3
    """
    if webSearchTool_provider == "Tavily":
        webSearchTool = TavilySearchResults(
            api_key = api_key,
            max_results = max_results,
            search_depth="advanced"
        )
    

    return webSearchTool



def instantiate_webSearchTool_main():
    """Instantiate the selected webSearchTool model."""
    try:
        if st.session_state.webSearchTool_provider == "Tavily" and st.session_state.webSearchTool_api_key.startswith("tvly-"):
            webSearchTool = instantiate_webSearchTool(
                "Tavily",
                api_key=st.session_state.webSearchTool_api_key,
                max_results=st.session_state.max_results,
            )
        else:
            raise ValueError("webSearchTool Api key is not provided or is incorrect!")
    except Exception as e:
        st.error(f"An error occured: {e}")
        webSearchTool = None
    
    return webSearchTool