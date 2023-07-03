
import chainlit as cl
from langchain import PromptTemplate, LLMChain, HuggingFaceHub
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

repo_id = "tiiuae/falcon-7b"  
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.6, "max_length": 2000})

templates = """
Question: {question}

Answer: 
"""

@cl.langchain_factory(use_async=True) 
def factory():
    prompt = PromptTemplate(template=templates, input_variables=['question'])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)
    return llm_chain

@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: str):
    # this is an intermediate step
    await cl.Message(author="Tool 1", content=f"Response from tool1", indent=1).send()

    # send back the final answer
    await cl.Message(content=f"This is the final answer").send()



