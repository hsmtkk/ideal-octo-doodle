from langchain_openai import ChatOpenAI
from langchain.chains.summarize.chain import load_summarize_chain
import forth_embedding

docs = forth_embedding.load_docs()
llm = ChatOpenAI()
chain = load_summarize_chain(llm, "map_reduce")
result = chain.invoke(docs)
print(result)
