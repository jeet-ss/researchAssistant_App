from functools import partial

from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import MemorySaver

from utils.analyst_utils import create_analysts, human_feedback, should_continue
from utils.interview_utils import generate_answer, generate_question, search_web, \
                                        search_wikipedia, save_interview, route_messages, initiate_all_interviews
from utils.writer_utils import write_section, write_report, write_introduction, write_conclusion, finalize_report
from models.states import ResearchGraphState, InterviewState




def create_ra_graph(llm, webSearchTool):
    ### Create analysts
    # analyst_creator = StateGraph(GenerateAnalystsState)
    # analyst_creator.add_node("create_analysts", create_analysts)
    # analyst_creator.add_node("human_feedback", human_feedback)
    # analyst_creator.add_edge(START, "create_analysts")
    # analyst_creator.add_edge("create_analysts", "human_feedback")
    # analyst_creator.add_conditional_edges("human_feedback", should_continue, ["create_analysts", END])
    # Compile 
    # memory = MemorySaver()
    # analyst_graph = analyst_creator.compile(interrupt_before=['human_feedback'], checkpointer=memory)

    # Add nodes and edges 
    interview_builder = StateGraph(InterviewState)
    interview_builder.add_node("ask_question", partial(generate_question, llm=llm))
    interview_builder.add_node("search_web", partial(search_web, llm=llm, webSearchTool=webSearchTool))
    interview_builder.add_node("search_wikipedia", partial(search_wikipedia, llm=llm))
    interview_builder.add_node("answer_question", partial(generate_answer, llm=llm))
    interview_builder.add_node("save_interview", save_interview)
    interview_builder.add_node("write_section", partial(write_section, llm=llm))

    # Flow
    interview_builder.add_edge(START, "ask_question")
    interview_builder.add_edge("ask_question", "search_web")
    interview_builder.add_edge("ask_question", "search_wikipedia")
    interview_builder.add_edge("search_web", "answer_question")
    interview_builder.add_edge("search_wikipedia", "answer_question")
    interview_builder.add_conditional_edges("answer_question", route_messages,['ask_question','save_interview'])
    interview_builder.add_edge("save_interview", "write_section")
    interview_builder.add_edge("write_section", END)

    # Interview 
    # memory = MemorySaver()
    # interview_graph = interview_builder.compile(checkpointer=memory).with_config(run_name="Conduct Interviews")
    # # invoke 
    # interview = interview_graph.invoke({"analyst": analysts[0], "messages": messages, "max_num_turns": 2}, thread)

    # Add nodes and edges 
    builder = StateGraph(ResearchGraphState)
    builder.add_node("create_analysts", partial(create_analysts, llm=llm))
    builder.add_node("human_feedback", human_feedback)
    builder.add_node("conduct_interview", interview_builder.compile())
    builder.add_node("write_report",partial(write_report, llm=llm))
    builder.add_node("write_introduction",partial(write_introduction, llm=llm))
    builder.add_node("write_conclusion",partial(write_conclusion, llm=llm))
    builder.add_node("finalize_report",finalize_report)

    # Logic
    builder.add_edge(START, "create_analysts")
    builder.add_edge("create_analysts", "human_feedback")
    builder.add_conditional_edges("human_feedback", initiate_all_interviews, ["create_analysts", "conduct_interview"])
    builder.add_edge("conduct_interview", "write_report")
    builder.add_edge("conduct_interview", "write_introduction")
    builder.add_edge("conduct_interview", "write_conclusion")
    builder.add_edge(["write_conclusion", "write_report", "write_introduction"], "finalize_report")
    builder.add_edge("finalize_report", END)

    # Compile
    memory = MemorySaver()
    graph = builder.compile(interrupt_before=['human_feedback'], checkpointer=memory)

    return graph