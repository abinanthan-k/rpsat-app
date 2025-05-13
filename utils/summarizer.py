from langchain.chat_models import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def summarize(text):
    prompt = PromptTemplate.from_template("Summarize this research paper:\n\n{text}")
    model = ChatGoogleGenerativeAI(model="gemini-pro")
    chain = LLMChain(llm=model, prompt=prompt)
    return chain.run(text=text)
