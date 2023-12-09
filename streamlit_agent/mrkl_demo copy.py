import streamlit as st

from langchain.agents import AgentType, initialize_agent, Tool
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chains import LLMMathChain

from langchain.chat_models import AzureChatOpenAI

from streamlit_agent.callbacks.capturing_callback_handler import playback_callbacks
from streamlit_agent.clear_results import with_clear_container

# title
st.set_page_config(
    page_title="一个有梗的电商", page_icon="🤣", layout="wide", initial_sidebar_state="collapsed"
)

"# 🤣 有梗 AI\n> 我是一个有梗的电商"

# llm
llm = AzureChatOpenAI(
    openai_api_version="2023-12-01-preview",
    openai_api_base="https://autoagents-ca-east.openai.azure.com/",
    deployment_name="gpt-4",
    streaming=True,
)

# tools
llm_math_chain = LLMMathChain(llm=llm)
tools = [
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
    )
]

# agent
agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True)

# conversation

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(placeholder="您想整啥点啊？T 恤, 水杯, 帆布袋"):
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(prompt, callbacks=[st_callback])
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
