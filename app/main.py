

from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate


def main():
    pass

if __name__ == '__main__':
    main()



# prompt_template = ChatPromptTemplate.from_template(review_template)
# messages = prompt_template.format_messages(text=customer_review)

prompt = ChatPromptTemplate.from_template(template=review_template_2)

messages = prompt.format_messages(text=customer_review, 
                                format_instructions=format_instructions)

# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
chat = ChatOpenAI(temperature=0.0)

# memory = ConversationBufferMemory()
memory = ConversationBufferWindowMemory(k=10)
memory = ConversationTokenBufferMemory(llm=chat, max_token_limit=30)
memory = ConversationSummaryBufferMemory(llm=chat, max_token_limit=100)

memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})

memory.load_memory_variables({})

conversation = ConversationChain(
    llm=chat,
    memory = memory,
    verbose=True
)

conversation.predict(input="What would be a good demo to show?")

response = chat(messages)
output_dict = output_parser.parse(response.content)
type(output_dict)
output_dict.get('delivery_days')