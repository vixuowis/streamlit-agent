from langchain.chains.openai_functions import (
    create_structured_output_chain,
)
from langchain.prompts import ChatPromptTemplate

from langchain.tools import tool

from langchain.pydantic_v1 import BaseModel, Field

from streamlit_agent.models.gpt import get_llm


class Response(BaseModel):
    """根据产品名称返回一些梗"""

    memes_list: list[str] = Field(..., description="梗的文字，列表形式返回")


@tool("搜索爆梗")
def get_memes_chain(input: str) -> list[str]:
    """get memes by llm chain."""

    # If we pass in a model explicitly, we need to make sure it supports the OpenAI function-calling API.
    llm = get_llm(is_streaming=False)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                我的目标：
                通过对提供的搜索数据进行分析，发掘适合印在 T 恤上的梗，允许搭配 emoji，并以 Markdown 格式输出，约 5-10 个。
                从最近的网络潮流中提取有趣的梗（Meme），并以中文文字形式输出，主要从中文互联网中搜索。

                输出格式：
                ```
                ["#热梗文字1", "#热梗文字2"]
                ```
                """,
            ),
            ("human", "Use the given format to response from the following input: {input}"),
            ("human", "Tip: Make sure to answer in the correct format"),
        ]
    )

    chain = create_structured_output_chain(Response, llm, prompt)
    response = chain.run({"input": input})
    print("response = ", response)

    return response
