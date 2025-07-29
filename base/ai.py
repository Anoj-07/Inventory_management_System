from groq import Groq
import os

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def create_description_with_ai(product_name):   
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
        {
            "role": "system",
            "content": "Act as a Description generator by product name for my IMS system. It should be a precise description not any extra thing"
        },
        {
            "role": "user",
            "content": "laptop"
        },
        {
            "role": "assistant",
            "content": "Portable personal computer designed for mobile use, typically featuring a compact keyboard, display, and processing components."
        },
        {
            "role": "user",
            "content": ""
        }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content


