from openai import OpenAI

def start():
    qry = input("ask you query on cricket:\n")
    # print(qry)

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful cricket statistics assistant."},
            {
                "role": "user",
                "content": qry
            }
        ]
    )

    print(completion.choices[0].message)