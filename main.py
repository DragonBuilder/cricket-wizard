import typer
from openai import OpenAI

openai_api_key = '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'


def start():
    qry = input("ask you query on cricket:\n")
    # print(qry)

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": qry
            }
        ]
    )

    print(completion.choices[0].message)


if __name__ == "__main__":
    typer.run(start)