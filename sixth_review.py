# https://python.langchain.com/v0.2/docs/versions/migrating_chains/map_reduce_chain/
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import forth_embedding

docs = forth_embedding.load_docs()
llm = ChatOpenAI()

# Map
map_template = (
    "Here is one of a chapter from a book. Read it and write a review: {docs}."
)
map_prompt = ChatPromptTemplate(
    [("system", "You are a well experienced system engineer."), ("human", map_template)]
)
map_chain = LLMChain(llm=llm, prompt=map_prompt)

# Reduce
reduce_template = """
The following is a set of reviews of a book:
{docs}
Take these and distill it into a final, consolidated review of the book.
Also give me the score of  the book out of 5.
0 means not recommended, 5 means strongly recommended.
"""
reduce_prompt = ChatPromptTemplate(
    [
        ("system", "You are a well experienced system engineer."),
        ("human", reduce_template),
    ]
)
reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

# Takes a list of documents, combines them into a single string, and passes this to an LLMChain
combine_documents_chain = StuffDocumentsChain(
    llm_chain=reduce_chain, document_variable_name="docs"
)

# Combines and iteratively reduces the mapped documents
reduce_documents_chain = ReduceDocumentsChain(
    # This is final chain that is called.
    combine_documents_chain=combine_documents_chain,
    # If documents exceed context for `StuffDocumentsChain`
    collapse_documents_chain=combine_documents_chain,
    # The maximum number of tokens to group documents into.
    token_max=1000,
)

map_reduce_chain = MapReduceDocumentsChain(
    # Map chain
    llm_chain=map_chain,
    # Reduce chain
    reduce_documents_chain=reduce_documents_chain,
    # The variable name in the llm_chain to put the documents in
    document_variable_name="docs",
    # Return the results of the map steps in the output
    return_intermediate_steps=False,
)

result = map_reduce_chain.invoke(docs)
print(result)
print(result["output_text"])
