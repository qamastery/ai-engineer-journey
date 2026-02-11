from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": "You are a senior QA engineer."},
        {"role": "user", "content": "Generate 5 test cases for login functionality."}
    ],
    temperature=0.3,
)

print(response.choices[0].message.content)
