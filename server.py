from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyBAC3Q5Bukp7rtZ6xmExAe1VDtWFvrgczA")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/process', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get('message', '')
    
    response = model.generate_content(message)
    # Logic to process the message
    response_message = f"Клим говорит: {response}"

    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
