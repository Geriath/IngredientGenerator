import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def basic():
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=generate_prompt(),
    temperature=0.8,
    max_tokens=500,
)
    result = response.choices[0].text
    splitresult = result.splitlines()
    splitstring = splitresult[0]
    bonk = len(splitstring)
    name = splitstring[6:bonk]
    f = open("Results/"+name+".txt", "a")
    f.write(result)
    f.close()
    return result

def generate_prompt():
    return """Generate a fictional fantasy alchemy ingredient based on the real world plants, animals, fungi or minerals. 
Name: (The name of the ingredient) 
Latin Name: (The name of the ingredient in Latin) 
Description: (What it looks like) 
Element: (Fire, Water, Earth, Air or other)
Location: (Where can it be found) 
Obtaining Method: (What is the method of obtaining the ingredient)
Rarity: (How rare it is) 
Uses: (What could it be used for in fantasy alchemy)"""

basic()