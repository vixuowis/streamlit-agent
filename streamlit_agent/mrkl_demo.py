import os

from pathlib import Path

import streamlit as st

from langchain import SQLDatabase
from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool, load_tools
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chains import LLMMathChain

# from langchain.llms import OpenAI
from langchain.chat_models import AzureChatOpenAI
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from langchain_experimental.sql import SQLDatabaseChain

from streamlit_agent.callbacks.capturing_callback_handler import playback_callbacks
from streamlit_agent.clear_results import with_clear_container

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()

SAVED_SESSIONS = {
    "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?": "leo.pickle",
    "What is the full name of the artist who recently released an album called "
    "'The Storm Before the Calm' and are they in the FooBar database? If so, what albums of theirs "
    "are in the FooBar database?": "alanis.pickle",
}

st.set_page_config(
    page_title="有梗 AI", page_icon="🦜", layout="wide", initial_sidebar_state="collapsed"
)

"# 🦜🔗 有梗 AI"

# Tools setup
llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    openai_api_base="https://autoagents-ca-east.openai.azure.com/",
    deployment_name="gpt-4",
    streaming=True,
)

# Initialize agent
llm_math_chain = LLMMathChain(llm=llm)
tools = [
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
        return_direct=True,
    )
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

with st.form(key="form"):
    user_input = st.text_input("您想要点啥啊？")
    submit_clicked = st.form_submit_button("开始找点乐子！")

output_container = st.empty()
if with_clear_container(submit_clicked):
    output_container = output_container.container()
    output_container.chat_message("user").write(user_input)

    answer_container = output_container.chat_message("有梗 AI", avatar="🦜")
    st_callback = StreamlitCallbackHandler(answer_container)

    # If we've saved this question, play it back instead of actually running LangChain
    # (so that we don't exhaust our API calls unnecessarily)
    answer = agent.run(user_input, callbacks=[st_callback])

    answer_container.write(answer)
