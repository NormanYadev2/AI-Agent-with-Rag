from langchain.tools import Tool
from vector import retriever

# Wrap retriever in a tool so the agent can use it
def retrieve_reviews(question: str) -> str:
    docs = retriever.invoke(question)
    return "\n".join([doc.page_content for doc in docs])

# Agent tool definition
review_tool = Tool(
    name="RestaurantReviewRetriever",
    func=retrieve_reviews,
    description="Useful for answering questions about a pizza restaurant using customer reviews."
)
