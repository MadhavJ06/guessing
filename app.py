from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Game data with questions and correct answers
QUESTIONS = [
    {
        "id": 1,
        "date": "22 July",
        "correct_answer": "First day we met",
        "options": [
            "First time you fell for me",
            "First day we met",
            "First time I fell for you",
            "First day you kicked my ass"
        ]
    },
    {
        "id": 2,
        "date": "27 August", 
        "correct_answer": "First time we told I love you",
        "options": [
            "First time you ran away with me",
            "First time we kissed",
            "First time I won over your heart",
            "First time we told I love you"
        ]
    },
    {
        "id": 3,
        "date": "19 Aug 22",
        "correct_answer": "First CPR",
        "options": [
            "First CPR",
            "First medical emergency",
            "First aid training",
            "First suture"
        ]
    },
    {
        "id": 4,
        "date": "11 Jun 23",
        "correct_answer": "Graduation",
        "options": [
            "Kitty party",
            "Moving out of our house",
            "Graduation",
            "Promotion"
        ]
    },
    {
        "id": 5,
        "date": "28 April 24",
        "correct_answer": "Consultant said sorry",
        "options": [
            "Left MGM",
            "Consultant said sorry",
            "Got leave from work without any issues",
            "Got paycheck"
        ]
    },
    {
        "id": 6,
        "date": "14/01/25",
        "correct_answer": "Told Family about us",
        "options": [
            "Holiday celebration",
            "went on family outing",
            "Family dinner",
            "Told Family about us",
        ]
    }
]

@app.route('/')
def index():
    return render_template('game.html', questions=QUESTIONS)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_id = int(data['question_id'])
    user_answer = data['answer']
    
    # Find the question
    question = next(q for q in QUESTIONS if q['id'] == question_id)
    
    if user_answer == question['correct_answer']:
        return jsonify({
            'correct': True,
            'message': 'Correct! Here, have a kitten 💕',
            'answer': question['correct_answer']
        })
    else:
        return jsonify({
            'correct': False,
            'message': 'Oops! Kitten in jail, Try again or reveal answer 😊',
            'answer': question['correct_answer']
        })

@app.route('/reveal_answer', methods=['POST'])
def reveal_answer():
    data = request.json
    question_id = int(data['question_id'])
    
    question = next(q for q in QUESTIONS if q['id'] == question_id)
    
    return jsonify({
        'answer': question['correct_answer'],
        'message': f"The answer is: {question['correct_answer']} 💝"
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
