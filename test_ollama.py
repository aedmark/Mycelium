from mycelium.llm import OllamaInterface
llm = OllamaInterface(model="mistral-nemo:latest") # Assume this is the model
res = llm.generate("Say 'Hello Mycelium' and nothing else.")
print(f"Ollama says: {res}")
