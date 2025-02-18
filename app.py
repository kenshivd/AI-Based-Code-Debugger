from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/debug", methods=["POST"])
def debug_code():
    code_snippet = request.json["code"]
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze and debug the following code:\n{code_snippet}",
        max_tokens=150
    )

    return jsonify({"debug_suggestions": response["choices"][0]["text"].strip()})

if __name__ == "__main__":
    app.run(debug=True)
