# TEXT2text.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

# Set model name (you can change this to "t5-small" or any other compatible model)
model_name = "google/flan-t5-base"

# Load tokenizer and model
print("🔄 Loading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Use MPS on Mac if available
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model = model.to(device)
print(f"✅ Model loaded. Using device: {device}")

# Create the text2text pipeline
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=0 if torch.backends.mps.is_available() else -1)

# Start prompt loop
print("\n📝 Text-to-Text Generator is ready!")
print("Type your prompt below. Type 'exit' to quit.\n")

while True:
    prompt = input("👉 Prompt: ")
    if prompt.strip().lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    output = pipe(prompt, max_length=256, do_sample=True)
    print("🤖 Output:", output[0]['generated_text'], "\n")
