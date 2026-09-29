from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ('system', 'please in a {tone} tone, give an announcement for {audience} with details {announcement_details}'),
    ('human', '{announcement_details}')
])