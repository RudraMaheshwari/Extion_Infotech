from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm a bot, so I'm always good. How about you?"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created for this demonstration."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response_route():
    user_text = request.args.get('msg')
    return jsonify(response=get_bot_response(user_text))

if __name__ == "__main__":
    app.run(debug=True)
