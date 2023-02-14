import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt,
            temperature=0.75,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt():
    return """Generate a fictional fantasy alchemy ingredient based on the real world plants, animals, fungi or minerals. 
Name: (The name for the ingredient) 
Latin Name:
Description: (What it looks like) 
Location: (Where can it be found) 
Rarity: (How rare it is) 
Uses: (What could it be used for in fantasy alchemy)"""
