import httpx
import os
from dotenv import load_dotenv

load_dotenv()

def send_chat_completion_request(messages):
    url = "https://api.openai.com/v1/chat/completions"
    data = {
        "model": "gpt-4o",
        "messages": messages
    }
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json"
    }

    response = httpx.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print("Error (", response.status_code, "): ", response.text)
        return

    return response.json()


if __name__ == "__main__":
    messages = [
        {
            "role": "user",
            "content": "You are in a debate. You will defend your position ardently. Your responses will be at most three sentences. The debate will end when you decide the other person's arguments have persuaded you to change your position. The debate may not end with such an outcome and may require a debate moderator to declare the debate over. The topic is Chevy vs Ford. Your position is Ford is better than Chevy. Your opponent has said: Chevy offers better overall performance and reliability than Ford, making it a superior choice. The range of models, from trucks to compact cars, outshines Ford in terms of innovation and design. Chevy's vehicles also come with a stronger reputation for durability and long-term value. Respond to your opponent. "
        }
    ]

    response = send_chat_completion_request(messages)
    print("response", response)