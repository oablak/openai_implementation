import openai
import os


while True:
    model_engine = "davinci-002"
    user_prompt = input()
    if "exit" in user_prompt or "quit" in user_prompt:
        break

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=user_prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0,
    )

    response = completion.choices[0].text

    print(response)
