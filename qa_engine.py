from groq import Groq
import os
# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context_chunks,question):
    context="\n\n".join(context_chunks)
    prompt=f"""
    You are a document assistant.
    Answer the question ONLY using the provided context.
    If the answer is not present in the context, say:
    "The answer is not found in the provided document."
    Context:
    {context}
    Question:
    {question}
    """
    response = client.chat.completions.create(
        # Llama 3.3 70b is highly recommended for RAG tasks on Groq
        model="llama-3.3-70b-versatile", 
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0 # Keep at 0 for factual accuracy
    )

    return response.choices[0].message.content