from flask import Flask, request, jsonify
import google.generativeai as genai
import re
from random import *

app = Flask(__name__)

# Replace with your actual API endpoint and key for Google Gemini
API_KEY = "AIzaSyBAC3Q5Bukp7rtZ6xmExAe1VDtWFvrgczA"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/process', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get('message', '')
    
    StathamPattern = r"т[еэ]тх[еэ]м"
    StathamQuotes = [
                    "Судно знаешь? Я засудил", 
                     "Тихий океан знаешь? Я усмирил", 
                     "Соединённые Штаты знаешь? Я соединил", 
                     "Мы должны оставаться мыми, а они – оними",
                     "Если заблудился в лесу, иди домой",
                     "В жизни всегда есть две дороги: одна — первая, а другая — вторая",
                     "Делай, как надо. Как не надо, не делай",
                     "Работа — это не волк. Работа — ворк. А волк — это ходить",
                     "Марианскую впадину знаешь? Это я упал",
                     "Не будьте эгоистами, в первую очередь думайте о себе!",
                     "Работа не волк. Никто не волк. Только волк волк"
                     ]
    if re.search(StathamPattern, message, re.IGNORECASE):
        chosen_quote = StathamQuotes[randint(0, len(StathamQuotes)-1)]
        return jsonify({'response': chosen_quote})

    Patterns2 = r"себе"
    Patterns2Answers = [
                        "Когда я захожу в зал тренажёр делает отжимания",
                        "Когда я открываю окно, окно становится прохлодным",
                        "ө"
                     ]
    if re.search(Patterns2, message, re.IGNORECASE):
        chosen_quote = Patterns2Answers[randint(0, len(Patterns2Answers)-1)]
        return jsonify({'response': chosen_quote})

    Patterns3 = r"предск"
    Patterns3Answers = [
                        "Да",
                        "Нет",
                        "Возможно",
                        "Да нет наверное",
                        "Определённо нет",
                        "Определённо да",
                        "В принципе можно",
                        "В принципе можно",
                        "В принципе можно",
                        "В принципе можно",
                        "Не будем исключать"
                     ]
    if re.search(Patterns3, message, re.IGNORECASE):
        chosen_quote = Patterns3Answers[randint(0, len(Patterns3Answers)-1)]
        return jsonify({'response': chosen_quote})
    
    gemini_response = model.generate_content(message)
    response = gemini_response.text
    response = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", response)
    response = re.sub(r"(?<!\*)\*(?!\*)", "<br>", response)
    # Logic to process the message
    response_message = f"Клим говорит: {response}"

    potomus = ["Потому что", "Покачену", "Вот так вот", "Вопросы?", "А ну в общем значит слушай значит смотри значит в общем слушай это самое мда", "Я тебе запрещаю задовать вопросы.", "ъуъ", "ъ", "🤌🏻🤌🏻", "ө"]
    potomu = randint(1,2)
    msg = potomus[randint(0, len(potomus)-1)]
    if potomu == 1:
        return jsonify({'response': response_message})
    else:
        return jsonify({'response': msg})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

