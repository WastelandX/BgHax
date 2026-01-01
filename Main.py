import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


model_name = "EleutherAI/gpt-neo-2.7B"  # You can change this to any model you prefer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_text(prompt, max_length=50):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def main():
    print("Welcome to the Uncensored AI Tool!")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = generate_text(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()