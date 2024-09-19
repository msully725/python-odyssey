from dataclasses import dataclass, field
import chat_completion_api as api

@dataclass
class ChatMessage:
    content: str
    role: str = "user"

    def to_dict(self):
        return { "role": self.role, "content": self.contet }

@dataclass
class ChatThread:
    messages: list[ChatMessage] = field(default_factory=list)

    def to_request(self):
        return [message.__dict__ for message in self.messages]

debaterOneThread = ChatThread()
debaterOneThread.messages = [
    ChatMessage("You are in a debate. You will defend your position ardently. Your responses will be at most three sentences. The debate will end when you decide the other person's arguments have persuaded you to change your position. The debate may not end with such an outcome and may require a debate moderator to declare the debate over. The topic is Chevy vs Ford. Your position is Chevy is better than Ford. Start the debate and make your claim on your position.")
]

debaterTwoThread = ChatThread()
debaterTwoThread.messages = [
    ChatMessage("You are in a debate. You will defend your position ardently. Your responses will be at most three sentences. The debate will end when you decide the other person's arguments have persuaded you to change your position. The debate may not end with such an outcome and may require a debate moderator to declare the debate over. The topic is Chevy vs Ford. Your position is Ford is better than Chevy. Your opponent has said: ")
]

response = api.send_chat_completion_request(debaterOneThread.to_request())
print(response)