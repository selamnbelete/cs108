import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "your system prompt here"},
        {"role": "user",   "content": "your request here"},
    ]
)
text = response["message"]["content"]
