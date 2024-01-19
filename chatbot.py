# pip install transformers
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class SimpleChatbot:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def chat(self, user_input):
        input_ids = self.tokenizer.encode(user_input, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

def main():
    chatbot = SimpleChatbot()

    print("Chatbot: Hello! I'm a chatbot made by using transformer library. You can start chatting with me. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = chatbot.chat(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

