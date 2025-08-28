# Use a pipeline as a high-level helper
import transformers

from transformers import pipeline
import torch

# Load model with pipeline
pipe = pipeline(
    "text-generation",
    model="LiquidAI/LFM2-700M",
    device_map="auto",
    torch_dtype=torch.float32   # safer on Mac MPS
)

print("🤖 Text Generator Ready! Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit", "q"]:
        print("Goodbye! 👋")
        break

    # Generate text
    output = pipe(prompt, max_new_tokens=100, do_sample=True, top_p=0.9, temperature=0.7)
    print("AI:", output[0]["generated_text"], "\n")
