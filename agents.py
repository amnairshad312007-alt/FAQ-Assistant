import os
import json
from google import genai

# Yahan apni Gemini API key direct string mein daal dein
client = genai.Client(api_key="client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))")

def run_agent(system_prompt: str, user_input: str) -> str:
    full_prompt = f"System Instructions:\n{system_prompt}\n\nInput:\n{user_input}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt,
    )
    return response.text

# 1. FAQ Classifier Agent
def faq_classifier(customer_question: str) -> str:
    prompt = "You are a Question Classification Specialist. Understand the customer question and identify its category strictly from these options: shipping, returns, refunds, payments, or general."
    return run_agent(prompt, customer_question).strip().lower()

# 2. Knowledge Agent
def knowledge_agent(category: str) -> str:
    prompt = "You are an FAQ Knowledge Specialist. Based on the requested category, retrieve the relevant policy or information from the knowledge base."
    
    with open("knowledge_base.json", "r") as f:
        kb = json.load(f)
    
    kb_text = json.dumps(kb, indent=2)
    query = f"Category: {category}\n\nKnowledge Base:\n{kb_text}"
    return run_agent(prompt, query)

# 3. Response Agent
def response_agent(question: str, retrieved_info: str) -> str:
    prompt = "You are a Customer Support Specialist. Generate a clear, polite, and helpful response for the customer strictly grounded in the retrieved information. Avoid inventing answers when information is unavailable."
    query = f"Customer Question: {question}\n\nRetrieved Information:\n{retrieved_info}"
    return run_agent(prompt, query)