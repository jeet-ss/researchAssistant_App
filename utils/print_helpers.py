
def print_analysts(analysts, container=None):
    container.empty()
    analysts_list = analysts['analysts']
    divider = "-" * 50
    #print(analysts2)
    #analysts = event.get('analysts', '')
    if analysts_list:
        for analyst in analysts_list:
            container.text(f"Name: {analyst.name} \nAffiliation: {analyst.affiliation} \nRole: {analyst.role} \nDescription: {analyst.description} \n{divider} ")
            # st.write(f"Name: {analyst.name}")
            # st.write(f"Affiliation: {analyst.affiliation}")
            # st.write(f"Role: {analyst.role}")
            # st.write(f"Description: {analyst.description}")
            # st.write("-" * 50)  

def print_analysts_streamlit(analysts):
    pass