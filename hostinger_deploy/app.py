import os
import json
import logging
import random
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "magyar_quiz_secret_key")

# Load quiz questions from JSON file
def load_questions():
    with open('questions.json', 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/')
def index():
    # Initialize session if it doesn't exist
    if 'scores' not in session:
        session['scores'] = {
            "Nemzeti jelképek és ünnepek": 0,
            "Történelmi események": 0, 
            "Irodalom és zene": 0,
            "Alkotmányos intézmények": 0,
            "Állampolgári jogok és kötelességek": 0,
            "Vegyes kérdések": 0
        }
        session['completed'] = []
    
    # Calculate total score
    total_score = sum(session['scores'].values())
    max_score = 75  # 6 quizzes × 5 questions × 2.5 points
    
    return render_template('index.html', 
                           scores=session['scores'],
                           total_score=total_score,
                           max_score=max_score,
                           completed=session['completed'])

@app.route('/quiz/<quiz_name>')
def quiz(quiz_name):
    questions = load_questions()
    
    # Get questions for the selected quiz
    quiz_questions = [q for q in questions if q['theme'] == quiz_name]
    
    # Shuffle questions if they exist
    if quiz_questions:
        random.shuffle(quiz_questions)
    
    # Store questions in session for result processing
    session['current_quiz'] = {
        'name': quiz_name,
        'questions': quiz_questions
    }
    
    # Get theme in French if available
    theme_fr = quiz_questions[0]['theme_fr'] if quiz_questions and 'theme_fr' in quiz_questions[0] else quiz_name
    
    return render_template('quiz.html', 
                           quiz_name=quiz_name, 
                           quiz_name_fr=theme_fr,
                           questions=quiz_questions,
                           language='fr')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if 'current_quiz' not in session:
        return redirect(url_for('index'))
    
    quiz_name = session['current_quiz']['name']
    questions = session['current_quiz']['questions']
    
    # Calculate score
    score = 0
    user_answers = []
    
    for i, question in enumerate(questions):
        answer_key = f'question_{i}'
        user_answer = request.form.get(answer_key, '')
        
        # Check if the answer is in French or Hungarian
        correct = False
        if 'correct_answer_fr' in question and user_answer == question['correct_answer_fr']:
            correct = True
        elif user_answer == question['correct_answer']:
            correct = True
        
        # Prepare answer data with both languages if available
        answer_data = {
            'question': question['question'],
            'question_fr': question.get('question_fr', question['question']),
            'user_answer': user_answer,
            'correct_answer': question['correct_answer'],
            'correct_answer_fr': question.get('correct_answer_fr', question['correct_answer']),
            'explanation': question['explanation'],
            'explanation_fr': question.get('explanation_fr', question['explanation']),
            'correct': correct,
            'options': question['options'],
            'options_fr': question.get('options_fr', question['options'])
        }
        
        user_answers.append(answer_data)
        
        # Add points for correct answers
        if correct:
            score += 2.5
    
    # Save score and mark quiz as completed
    session['scores'][quiz_name] = score
    if quiz_name not in session['completed']:
        session['completed'].append(quiz_name)
    session.modified = True
    
    # Get theme in French if available
    theme_fr = questions[0]['theme_fr'] if questions and 'theme_fr' in questions[0] else quiz_name
    
    # Prepare result data
    result_data = {
        'quiz_name': quiz_name,
        'quiz_name_fr': theme_fr,
        'score': score,
        'max_score': len(questions) * 2.5,
        'answers': user_answers,
        'language': 'fr'
    }
    
    return render_template('result.html', result=result_data)

@app.route('/reset_scores')
def reset_scores():
    if 'scores' in session:
        session.pop('scores')
    if 'completed' in session:
        session.pop('completed')
    return redirect(url_for('index'))
