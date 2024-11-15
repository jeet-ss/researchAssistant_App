import streamlit as st
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

from models.constants import ROOT
from models.graph import create_ra_graph
from utils.print_helpers import print_analysts
from utils.sidebar import app_sidebar
from utils.llms import instantiate_LLM_main
from utils.webSearchTool import instantiate_webSearchTool_main


explaination_text_header = """
### What is it About?

The **Research Assistant App** is an open-source project designed to streamline the research process. It acts as a virtual research assistant, capable of conducting interviews, generating insightful questions, and synthesizing information into comprehensive reports. Users can select and modify various personas and set the maximum number of interviews they wish to conduct.

For more details, visit:
"""
explaination_text_footer = """
#### Key Features:
- **AI Analyst Personas:** Tailor your research experience with customizable AI personas.
- **Parallel Web Search Capabilities:** Conduct multiple web searches simultaneously for efficient data gathering.
- **User-Friendly Interface:** Navigate easily through the app for a seamless research experience.

This tool is ideal for researchers, students, and professionals seeking efficient and organized data collection and analysis. 

"""


def refresh_func(container):
    # Clears the contents of the specified container
    container.empty()


def toggle_st():
    # Toggles the state of the application and resets relevant session state variables
    st.session_state.st = not st.session_state.st
    st.session_state.n = 0
    # Clear previous session data if it exists
    if 'report' in st.session_state:
        del st.session_state['report'] 
    if 'topic' in st.session_state:
        del st.session_state['topic'] 
    

def set_ss(key_list, value_list):
    # Sets session state values based on provided keys and values
    print(key_list, value_list)
    for i in range(len(key_list)):
        if value_list[i] == '~*~':
            # If value is a placeholder, retrieve the value from the widget
            value_list[i] = st.session_state['widget_' + key_list[i]]
            st.session_state[key_list[i]] = value_list[i]
        elif value_list[i] == '~*':
            # Store the current value for the key
            store_value(key_list[i])
        elif key_list[i] == 'n':
            # Special case for 'n' to handle specific logic
            if st.session_state['n'] > 0 and st.session_state['h_feedback'] == "":
                st.session_state[key_list[i]] = 7  # Set to a final stage if conditions are met
            else:
                st.session_state[key_list[i]] = value_list[i]
        else:
            # Set the session state for the key to the provided value
            st.session_state[key_list[i]] = value_list[i]

def store_value(key):
    # Stores the current value of the specified key in session state
    st.session_state[key] = st.session_state["_" + key]

def load_value(key):
    # Loads the value of the specified key from session state
    st.session_state["_" + key] = st.session_state[key]

def status_text(node_name):
    # Returns a status message based on the current node name
    if node_name == "conduct interview":
        return "Conducting Interviews..."
    elif node_name == "write_conclusion":
        return "Writing Conclusion..."
    elif node_name == "write_introduction":
        return "Writing Introduction"
    elif node_name == "write_report":
        return "Writing Report..."
    elif node_name == "finalize_report":
        return "Finalizing Report..."
    else:
        return None
    

def create_columns(cols: int):
    # Creates a specified number of empty columns and returns them as a list
    C_empty = []
    C = st.columns(cols)  # Create columns in Streamlit
    for col_num in range(len(C)):
        C_empty.append(C[col_num].empty())  # Append empty column to the list
    return C_empty

if __name__ == "__main__":
    # Set up the Streamlit app configuration
    st.set_page_config(page_title="Research App", page_icon="📖")
    st.title("📖 Research Assistant APP")

    app_sidebar()  # Initialize the sidebar for the app

    # Initialize session state variables if they do not exist
    if 'st' not in st.session_state:
        st.session_state.st = False  # Toggle state
    if 'n' not in st.session_state:
        st.session_state.n = 0  # Number of triggers
    if 'max_analysts' not in st.session_state:
        st.session_state.max_analysts = 3  # Default max analysts
    if 'topic' not in st.session_state:
        st.session_state.topic = ""  # Default topic
    if 'h_feedback' not in st.session_state:
        st.session_state.h_feedback = None  # Human feedback
    if 'max_rounds' not in st.session_state:
        st.session_state.max_rounds = 1  # Default max rounds
    if 'model_api_key' not in st.session_state:
        st.session_state.model_api_key = None  # API key for model
    if 'webSearchTool_api_key' not in st.session_state:
        st.session_state.webSearchTool_api_key = None  # API key for web search tool
    
    divider = "-" * 50  # Divider for display purposes
    
    def display_info():
        # Displays the current research query and configuration settings
        with queryDisplay_container:
            #st.write(f
            st.write(f':red[Research Query] : **{st.session_state["topic"]}**')
            analysts_col, rounds_col = st.columns(2)
            analysts_col.write(f':orange[Analysts Generated] : {st.session_state["max_analysts"]}')
            rounds_col.write(f':green[Max Interview Rounds] : {st.session_state["max_rounds"]}')

    # Configure memory for the application
    thread = {"configurable": {"thread_id": "1"}}

    # Streamlit UI components
    primary_button = st.container()  # Placeholder for the primary button
    queryDisplay_container = st.container(border=True)  # Container for displaying query info
    slate = st.empty()  # Placeholder for dynamic content
    slate.empty()  # Clear the slate
    main_container = slate.container()  # Main container for the app's content
    download_container = st.container()  # Container for download options

    # Display Start and Restart button based on the application state
    if st.session_state['st'] == False:
        with primary_button:
            git, start_butt, _ = create_columns(3)
            #git.page_link("https://github.com/jeet-ss/researchAssistant_App", label="Github Repository", icon=":material/code_blocks:")
            start_butt.button('Start', on_click=toggle_st, icon=":material/not_started:", type="primary")
        with main_container:
            st.write(explaination_text_header)
            _, git, _ = create_columns(3)
            git.page_link("https://github.com/jeet-ss/researchAssistant_App", label="Github Repository", icon=":material/code_blocks:")
            #st.page_link("https://github.com/jeet-ss/researchAssistant_App", label="Github Repository", icon=":material/code_blocks:")
            st.write(explaination_text_footer)
            
    else:
        if st.session_state['n'] != 7:
            primary_button.button('Re-Start', on_click=toggle_st, icon=":material/restart_alt:")

    # Start the application logic
    if st.session_state["st"] == True:
        
        if st.session_state['n'] == 0:
            if st.session_state.webSearchTool_provider == "Duck":
                st.session_state.webSearchTool_api_key = ""
            # Initial session: Load API keys and create the LLM and web search tool
            if st.session_state.model_api_key is not None and st.session_state.webSearchTool_api_key is not None:
                model = instantiate_LLM_main()  # Instantiate the language model
                webSearchTool = instantiate_webSearchTool_main()  # Instantiate the web search tool
                # Generate the graph at the start of the app
                if model is not None and webSearchTool is not None:
                    st.session_state.graph = create_ra_graph(llm=model, webSearchTool=webSearchTool, webSearchTool_provider=st.session_state.webSearchTool_provider) 
                    set_ss(['n'], [1])  # Move to the next state
                else:
                    st.info("Provide the Correct API Keys and Press Enter or Click Continue")
                    st.button("Continue", icon=":material/resume:")
            else:
                st.info("Provide the API Keys and Press Enter or Click Continue")
                st.button("Continue", icon=":material/resume:")

        if st.session_state['n'] == 1:
            # First session: Load input forms for user queries
            with main_container:
                with st.form('question', clear_on_submit=False):
                    st.text_input('Enter your question:', placeholder='What are PINNS?', key='_topic')
                    analysts_col, rounds_col = st.columns(2) 
                    with analysts_col:
                        st.slider("Choose Max no of Analysts to work on your topic: ",
                                   min_value=1, max_value=4, value=2, key='_max_analysts')
                    with rounds_col:
                        st.number_input("Enter max number of Interview Rounds :", key="_max_rounds",
                                        min_value=1, max_value=7, value=3)
                        
                    st.session_state.submitted = st.form_submit_button('Submit', on_click=set_ss, 
                                                                        args=(['n', 'topic', 'max_analysts', 'max_rounds'], [2, '~*', '~*', '~*']))

        elif st.session_state['n'] == 2:
            # Second session: Display the first output and wait for feedback
            if 'topic' in st.session_state:
                display_info()
            
            with main_container:
                analysts_container = st.container(key="analyst", border=True)
                C_empty = create_columns(st.session_state.max_analysts)  # Create columns for analysts
                
                # Load data from the LLM call
                with st.spinner("Calling LLMs...."):
                    for event in st.session_state.graph.stream({"topic": st.session_state['topic'], 
                                                                "max_analysts": st.session_state['max_analysts'], 
                                                                "max_num_turn": st.session_state["max_rounds"]},
                                                                thread, stream_mode="updates"):
                        analysts = event.get('create_analysts', '')
                        if analysts:
                            analysts_list = analysts['analysts']

                with analysts_container:
                    # Display the analysts' data
                    for col, analyst in zip(C_empty, analysts_list):
                        col.text(f'Name: {analyst.name} \nAffiliation: {analyst.affiliation} \nRole: {analyst.role} \nDescription: {analyst.description} \n{divider} \n{divider}') 
                
                # Display feedback form
                feedback_form = st.form('feedback', clear_on_submit=True)
                feedback_form.text_input("Feedback: ", placeholder="I want you to include someone from XYZ field in the conversation!", key="_h_feedback")
                st.session_state.submit_feedback = feedback_form.form_submit_button("Submit", 
                    on_click=set_ss, args=(['h_feedback', 'n'], ['~*', st.session_state['n'] + 1]))

        elif st.session_state['n'] > 2 and st.session_state['n'] < 6:
            # Third and subsequent sessions: Display last output and wait for feedback
            if 'topic' in st.session_state:
                display_info()            

            with main_container:
                analysts_container = st.container(key="analyst", border=True)
                C_empty = create_columns(st.session_state.max_analysts)  # Create columns for analysts

                # Load updated data from LLMs
                with st.spinner("Calling LLMs...."):
                    # Update graph with new human feedback
                    st.session_state.graph.update_state(thread, {"human_analyst_feedback": st.session_state['h_feedback']}, as_node="human_feedback")
                    
                    # Stream the graph for updates
                    for event in st.session_state.graph.stream(None, thread, stream_mode="updates"):
                        analysts = event.get('create_analysts', '')
                        if analysts:
                            analysts_list = analysts['analysts']
                        
                with analysts_container:
                    # Display the updated analysts' data
                    for col, analyst in zip(C_empty, analysts_list):
                        col.text(f'Name: {analyst.name} \nAffiliation: {analyst.affiliation} \nRole: {analyst.role} \nDescription: {analyst.description} \n{divider} \n{divider}') 

                # Display feedback form
                feedback_form = st.form('feedback', clear_on_submit=True)
                feedback_form.text_input("Feedback: ", placeholder="I want you to include someone from XYZ field in the conversation!", key="_h_feedback")
                st.session_state.submit_feedback = feedback_form.form_submit_button("Submit", 
                    on_click=set_ss, args=(['h_feedback', 'n'], ['~*', st.session_state['n'] + 1]))

        elif st.session_state['n'] == 7:
            # Final session: Generate and display the report
            if 'topic' in st.session_state:
                display_info()
                
            # Display the final report
            with main_container:
                if 'report' not in st.session_state:
                    with st.status("Preparing Final Report...") as status:
                        # Update graph to finalize the process
                        st.write("Finalizing Research Agents...")
                        st.session_state.graph.update_state(thread, {"human_analyst_feedback": None}, as_node="human_feedback")
                        st.write("Initiating Interviews...")
                        for event in st.session_state.graph.stream(None, thread, stream_mode="updates"):
                            # Print the name of the next node for information
                            node_name = next(iter(event.keys()))
                            print("--Node_name : ", node_name)
                            msg = status_text(node_name)
                            if msg is not None: 
                                st.write(msg)
                        
                        # Obtain the final report
                        final_state = st.session_state.graph.get_state(thread)
                        st.session_state['report'] = final_state.values.get('final_report')
                        # Update status to indicate completion
                        status.update(label="Report Complete!", state="complete", expanded=False)
                
                report_container = st.container(key="report", border=True)
                report_container.write(st.session_state['report'])  # Display the final report

            # Display download options for the report
            with download_container:
                C_empty = create_columns(3)  # Create columns for download options
                # Add download button for the report
                C_empty[0].download_button(label="Download Report", data=st.session_state.report, 
                                           file_name="researchAssistant_Report.md", mime="text/markdown", 
                                           type="primary", icon=":material/download:", key="download")
                C_empty[2].button('Re-Start', on_click=toggle_st, icon=":material/restart_alt:", type="primary")
                feedback = C_empty[1].feedback("stars")  # Collect feedback from the user
                if feedback is not None:
                    st.toast("Thank you for your Feedback!", icon=":material/done_all:")

# Debugging: Print the session state for inspection
#st.write(st.session_state)
