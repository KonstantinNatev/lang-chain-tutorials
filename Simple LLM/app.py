import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
model = ChatOpenAI(model="gpt-4")

parser = StrOutputParser()

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

template_result = prompt_template.invoke({"language": "German", "text": "How are you!"})

chain = prompt_template | model | parser

final_result = chain.invoke({"language": "German", "text": "How are you!"})
print("Final chain result:", final_result, "\n")
