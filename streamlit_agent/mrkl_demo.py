from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
import streamlit as st

from langchain.agents import Tool
from langchain.chains import LLMMathChain
from streamlit_agent.chains.memes import get_memes_chain
from streamlit_agent.chains.products import get_product_t2i

from streamlit_agent.models.gpt import get_llm

# title
st.set_page_config(
    page_title="一个有梗的电商", page_icon="🤣", layout="wide", initial_sidebar_state="collapsed"
)

st.title("🤣 有梗 AI - 一个有梗的电商")

# llm
llm = get_llm()

# memory
msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
)

# agent
llm_math_chain = LLMMathChain.from_llm(llm)
tools = [
    get_memes_chain,
    get_product_t2i,
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
    ),
]
chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)

# reset
if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
    msgs.clear()
    msgs.add_ai_message("恁想弄点啥？")
    st.session_state.steps = {}

# history
avatars = {"human": "user", "ai": "🤣"}
for idx, msg in enumerate(msgs.messages):
    with st.chat_message(avatars[msg.type]):
        # Render intermediate steps if any were saved
        for step in st.session_state.steps.get(str(idx), []):
            if step[0].tool == "_Exception":
                continue
            with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
                st.write(step[0].log)
                st.write(step[1])
        st.write(msg.content)

# chat
if prompt := st.chat_input(placeholder="T 恤, 水杯, 帆布袋"):
    st.chat_message("user").write(prompt)

    executor = AgentExecutor.from_agent_and_tools(
        agent=chat_agent,
        tools=tools,
        memory=memory,
        return_intermediate_steps=True,
        handle_parsing_errors=True,
    )

    with st.chat_message("assistant", avatar="🤣"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = executor(prompt, callbacks=[st_cb])
        st.markdown(response["output"])
        st.session_state.steps[str(len(msgs.messages) - 1)] = response["intermediate_steps"]
