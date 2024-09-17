# DebateGPT

Experimenting with a ChatGPT thread debating with another ChatGPT thread using OpenAI APIs.

## API via Postman
Initially using Postman to explore OpenAI APIs.

### Chat Completion

`POST https://api.openai.com/v1/chat/completions`

```json
{
    "model":"gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "Hi" 
        }
    ]
}
```

## Prompts

### Initial
```
You are in a debate.
You will defend your position ardently.
Your responses will be at most three sentences.
The debate will end when you decide the other person's arguments have persuaded you to change your position. 
The debate may not end with such an outcome and may require a debate moderator to declare the debate over. 
```

### Sample Topic and Positions

#### Sample Topic
Chevy vs Ford

#### Positions
Debator 1: Chevy is better than Ford

Debator2: Ford is better than Chevy

## Initial Implementation Plan
1. Set up to "threads", in this case, two Debator message arrays. 
2. Add the initial message to each message array. 
3. Prompt Debator 1 to start the debate and make their claim on their position. 
4. Append the message to Debator 2's messages, adding a prompt to respond to Debator 1's claim. 
5. Append the message to Debator 1's messages, adding a prompt to respond to Debator 2.
6. Repeat 4-5. 

How will we end? That's for a later iteration 😃

## Postman Sample

### 1. Debater 1 starting the debate
POST request:
```json
{
    "model":"gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "You are in a debate. You will defend your position ardently. Your responses will be at most three sentences. The debate will end when you decide the other person's arguments have persuaded you to change your position. The debate may not end with such an outcome and may require a debate moderator to declare the debate over. The topic is Chevy vs Ford. Your position is Chevy is better than Ford. Start the debate and make your claim on your position." 
        }
    ]
}
```

POST Response:
```json
{
    "id": "chatcmpl-A8ARu6YxMRZjwtnx7ex22Mb3wQLYp",
    "object": "chat.completion",
    "created": 1726510154,
    "model": "gpt-4o-2024-05-13",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Chevy offers better overall performance and reliability than Ford, making it a superior choice. The range of models, from trucks to compact cars, outshines Ford in terms of innovation and design. Chevy's vehicles also come with a stronger reputation for durability and long-term value.",
                "refusal": null
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 97,
        "completion_tokens": 55,
        "total_tokens": 152,
        "completion_tokens_details": {
            "reasoning_tokens": 0
        }
    },
    "system_fingerprint": "fp_25624ae3a5"
}
```

### 2. Debater 2 initial prompt for response to Debater 1

POST request:
```json
{
    "model":"gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "You are in a debate. You will defend your position ardently. Your responses will be at most three sentences. The debate will end when you decide the other person's arguments have persuaded you to change your position. The debate may not end with such an outcome and may require a debate moderator to declare the debate over. The topic is Chevy vs Ford. Your position is Ford is better than Chevy. Your opponent has said: Chevy offers better overall performance and reliability than Ford, making it a superior choice. The range of models, from trucks to compact cars, outshines Ford in terms of innovation and design. Chevy's vehicles also come with a stronger reputation for durability and long-term value. Respond to your opponent. " 
        }
    ]
}
```

POST Response:
```json
{
    "id": "chatcmpl-A8AZ0POuOM9PzlhOyDx47jEJwhZg5",
    "object": "chat.completion",
    "created": 1726510594,
    "model": "gpt-4o-2024-05-13",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Ford leads the industry with cutting-edge technology and engineering, particularly evident in their revolutionary EcoBoost engines, which provide superior performance and fuel efficiency. Additionally, Ford trucks, like the F-150, have consistently outsold Chevy's trucks, indicating a strong preference for Ford's durability and reliability among consumers. The longstanding heritage of iconic models like the Mustang further showcases Ford's commitment to innovation and design excellence.",
                "refusal": null
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 151,
        "completion_tokens": 80,
        "total_tokens": 231,
        "completion_tokens_details": {
            "reasoning_tokens": 0
        }
    },
    "system_fingerprint": "fp_25624ae3a5"
}
```

### 3. Debator 1 Response to Debator 2

POST request
```json
{
    "model":"gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "You are in a debate. You will defend your position ardently. Your responses will be at most three sentences. The debate will end when you decide the other person's arguments have persuaded you to change your position. The debate may not end with such an outcome and may require a debate moderator to declare the debate over. The topic is Chevy vs Ford. Your position is Chevy is better than Ford. Start the debate and make your claim on your position." 
        },
        {
            "role": "user",
            "content": "Your opponent has said: Ford leads the industry with cutting-edge technology and engineering, particularly evident in their revolutionary EcoBoost engines, which provide superior performance and fuel efficiency. Additionally, Ford trucks, like the F-150, have consistently outsold Chevy's trucks, indicating a strong preference for Ford's durability and reliability among consumers. The longstanding heritage of iconic models like the Mustang further showcases Ford's commitment to innovation and design excellence. Respond to your opponent."
        }
    ]
}
```

POST response
```json
{
    "id": "chatcmpl-A8Aa4wjs3154UDinP6zOoeXwowhBs",
    "object": "chat.completion",
    "created": 1726510660,
    "model": "gpt-4o-2024-05-13",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "While Ford's EcoBoost engines are impressive, Chevy offers the venerable Duramax diesel and V8 engines that deliver exceptional power and longevity, often preferred by heavy-duty truck users. Additionally, Chevy's Silverado and Colorado trucks consistently rank highly for reliability and performance in independent reviews. Lastly, Chevy's Corvette stands as a testament to American sports car innovation, rivaling, and often outperforming, the Mustang in both performance and luxury.",
                "refusal": null
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 191,
        "completion_tokens": 86,
        "total_tokens": 277,
        "completion_tokens_details": {
            "reasoning_tokens": 0
        }
    },
    "system_fingerprint": "fp_25624ae3a5"
}
```

### 4. Debator 2 response to Debator 1

POST request:
```json
{
    "model":"gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": "You are in a debate. You will defend your position ardently. Your responses will be at most three sentences. The debate will end when you decide the other person's arguments have persuaded you to change your position. The debate may not end with such an outcome and may require a debate moderator to declare the debate over. The topic is Chevy vs Ford. Your position is Ford is better than Chevy. Your opponent has said: Chevy offers better overall performance and reliability than Ford, making it a superior choice. The range of models, from trucks to compact cars, outshines Ford in terms of innovation and design. Chevy's vehicles also come with a stronger reputation for durability and long-term value. Respond to your opponent. " 
        },
        {
            "role": "user",
            "content": "Your opponent has said: While Ford's EcoBoost engines are impressive, Chevy offers the venerable Duramax diesel and V8 engines that deliver exceptional power and longevity, often preferred by heavy-duty truck users. Additionally, Chevy's Silverado and Colorado trucks consistently rank highly for reliability and performance in independent reviews. Lastly, Chevy's Corvette stands as a testament to American sports car innovation, rivaling, and often outperforming, the Mustang in both performance and luxury. Respond to your oppoenent."
        }
    ]
}
```

POST response:
```json
{
    "id": "chatcmpl-A8AeInU0h74wNrpw00VFoZ2NJVngh",
    "object": "chat.completion",
    "created": 1726510922,
    "model": "gpt-4o-2024-05-13",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Ford's F-Series trucks have been the best-selling trucks in America for over four decades, demonstrating superior reliability and popularity among consumers. Moreover, the Ford Mustang has a rich legacy and has consistently outperformed the Corvette in sales and maintains a reputation for blending performance with affordability. Lastly, Ford's commitment to innovation is evident in their cutting-edge electric vehicle offerings, such as the Mach-E and the upcoming F-150 Lightning, which surpass Chevy's current EV lineup in technological advancements and market excitement.",
                "refusal": null
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 253,
        "completion_tokens": 98,
        "total_tokens": 351,
        "completion_tokens_details": {
            "reasoning_tokens": 0
        }
    },
    "system_fingerprint": "fp_25624ae3a5"
}
```

### Observation
The current prompts appear to support an ongoing back and forth. Next up - automate this so that we can see how long this can go. Open question - will either debater ever cede to their opponenet? Will changing "ardently" change that?

# Next
* Research Implementation Options
  * API Request/Response
  * JSON Read/Write
  * Storage
     1. Std Out
     2. Flat file
     3. Database
     4. UI
