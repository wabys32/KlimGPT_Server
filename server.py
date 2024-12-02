from flask import Flask, request, jsonify
import google.generativeai as genai
import re

app = Flask(__name__)

# Replace with your actual API endpoint and key for Google Gemini
API_KEY = "AIzaSyBAC3Q5Bukp7rtZ6xmExAe1VDtWFvrgczA"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/process', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get('message', '')

    gemini_response = model.generate_content(message)
    response = gemini_response.text
    response = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", response)
    response = re.sub(r"(?<!\*)\*(?!\*)", "<br>", response)
    # Logic to process the message
    response_message = f"Клим говорит: {response}"

    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

