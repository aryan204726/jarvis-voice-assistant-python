from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-TX6XVmTfSLW3YeMcfW30dmuDdTf5sKUr2eYYCyYYrcZ_Wfa9quC-ro-ODSLnjT3BlbkFJZ12HyMlHcrCKPw-V-4fWAK-2gk7aiHkM4OIbs9wz6qtplST71dfl7RP7L2xUAJaBNJaf-70t4A" ,
    )

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant name Jarvis, skilled general tasks like alexa and google ."},
        {"role": "user", "content": "what is coding."}
    ]
)

print(completion.choices[0].message.content)
