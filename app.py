import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def basic():
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=generate_prompt(),
    temperature=0.75,
    temperature=0.8,
    max_tokens=300,
)
    result = response.choices[0].text
    f = open("test.txt", "a")
    f.write(result)
    f.close()
    return result

def generate_prompt():
    return """Generate a fictional fantasy alchemy ingredient based on the real world plants, animals, fungi or minerals. 
Name: (The name for the ingredient) 
Latin Name: (The name of the ingredient in latin)
Description: (What it looks like) 
Location: (Where can it be found) 
Rarity: (How rare it is) 
Uses: (What could it be used for in fantasy alchemy)"""