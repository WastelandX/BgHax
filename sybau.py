#!/usr/bin/env python3

import time

BANNER = """
===========================
  NIGGA GPT (Local CLI)
===========================
Type 'exit' to quit
"""

def fake_gpt_response(user_input):
    """
    This simulates ChatGPT logic.
    Later you can replace this with a real API.
    """
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello 👋 How can I help you today?"
    elif "who are you" in user_input:
        return "I am Sybau-GPT, a ChatGPT-like CLI tool made in Termux 😈"
    elif "python" in user_input:
        return "Python is a powerful language. Want help with scripts?"
    elif "bye" in user_input:
        return "Goodbye! Type 'exit' to leave."
    else:
        return "Interesting... tell me more 🤔"


def main():
    print(BANNER)

    while True:
        try:
            user_input = input("You > ")

            if user_input.strip().lower() == "exit":
                print("Sybau-GPT > Session ended 👋")
                break

            print("Sybau-GPT > thinking...")
            time.sleep(0.8)

            response = fake_gpt_response(user_input)
            print("Sybau-GPT >", response)

        except KeyboardInterrupt:
            print("\nSybau-GPT > Interrupted. Bye 👋")
            break


if __name__ == "__main__":
    main()