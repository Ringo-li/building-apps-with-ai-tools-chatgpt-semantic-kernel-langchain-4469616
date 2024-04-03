from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
  SystemMessagePromptTemplate,
  HumanMessagePromptTemplate,
  ChatPromptTemplate
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
chat_model = ChatOpenAI()
# print(chat_model.predict("Make the content more natural, and if there are errors, correct them and list them: Hi Team, the fresh XCC service data has been uploaded, please check."))

system_template = """You are an English teacher, please make the content more natural and if there are errors, please correct them and list them."""

system_message_promt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{text}"
human_massage_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_promt,human_massage_prompt])

class CommaSeparatedListOutParser(BaseOutputParser):
  def parse(self, text: str):
    return text.strip().split(", ")
  
chain = LLMChain(
  llm=ChatOpenAI(),
  prompt=chat_prompt,
  output_parser=CommaSeparatedListOutParser()
)

print(chain.run("What is the colours of the jeans?"))