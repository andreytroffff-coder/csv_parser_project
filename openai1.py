key = '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'

import openai
from openai import OpenAI

client = OpenAI(api_key=key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain what CSV files are"}
    ]
)

print(response.choices[0].message.content)

gemini_key = 'AIzaSyBR5_09zevOyabNV4Ncg25-VnjrO9nJfKs'