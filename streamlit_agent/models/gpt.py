from langchain.chat_models import AzureChatOpenAI


def get_llm(is_streaming=True):
    return AzureChatOpenAI(
        openai_api_version="2023-12-01-preview",
        openai_api_base="https://autoagents-ca-east.openai.azure.com/",
        deployment_name="gpt-4",
        streaming=is_streaming,
    )
