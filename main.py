from agents import faq_classifier, knowledge_agent, response_agent

def handle_customer_query(question: str):
    print("=" * 60)
    print(f"💬 Customer Question: {question}")
    print("=" * 60)

    # Step 1: Classify Question
    print("\n[1/3] FAQ Classifier is identifying category...")
    category = faq_classifier(question)
    print(f"✔ Identified Category: {category}")

    # Step 2: Retrieve Knowledge
    print("\n[2/3] Knowledge Agent is searching knowledge base...")
    retrieved_info = knowledge_agent(category)
    print("✔ Information retrieved successfully.")

    # Step 3: Generate Response
    print("\n[3/3] Response Agent is drafting final reply...")
    final_response = response_agent(question, retrieved_info)
    print("✔ Response generated.")

    print("\n" + "=" * 60)
    print("🤖 Final Support Response:")
    print("=" * 60)
    print(final_response)
    print("=" * 60)

if __name__ == "__main__":
    # Test customer question
    sample_question = "How many days will it take to get my money back after returning an item?"
    handle_customer_query(sample_question)