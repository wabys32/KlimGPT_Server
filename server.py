from flask import Flask, request, jsonify
import requests  # For making HTTP requests to Google Gemini (or equivalent AI API)

app = Flask(__name__)

# Replace with your actual API endpoint and key for Google Gemini
GEMINI_API_ENDPOINT = "https://api.google.com/gemini"
API_KEY = "AIzaSyBAC3Q5Bukp7rtZ6xmExAe1VDtWFvrgczA"

@app.route('/process', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get('message', '')

    gemini_response = call_gemini_api(message)
    # Logic to process the message
    response_message = f"Клим говорит: ответ на сообщение {gemini_response}"

    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True, port=5000)



def call_gemini_api(message):
    """
    Function to interact with Google Gemini API.
    :param message: Input message to send to the API
    :return: Response from Gemini
    """
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    payload = {
        'message': message,
    }
    try:
        response = requests.post(GEMINI_API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the response contains an error
        return response.json().get('response', "No response from Gemini")
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Gemini API: {e}"