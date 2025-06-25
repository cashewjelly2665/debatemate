from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/debate", methods=["POST"])
def debate():
    data = request.json
    topic = data.get("topic")
    stance = data.get("stance")

    prompt = f"You are DebateMate, an expert debate assistant. Give a strong argument for the stance '{stance}' on the topic '{topic}'."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"argument": response['choices'][0]['message']['content']})

@app.route("/")
def home():
    return "DebateMate API is running!"
