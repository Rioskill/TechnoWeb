from django.db import models

import random

TAGS = [
    'perl',
    'python',
    'TechnoPark',
    'MySQL',
    'django',
    'Firefox'
]

QUESTION_LEN = 100
ANSWER_LEN = 500

QUESTIONS = [
    {
        'title': f'Question {i}',
        'text': f'text {i}',
        'id': i,
        'tags': random.sample(TAGS, i % (len(TAGS) - 2) + 1),
        'rating': random.randint(-5, 100)
    }
    for i in range(1, QUESTION_LEN + 1)
]

ANSWERS = [
    {
        'question_id': random.randint(0, QUESTION_LEN),
        'text': f'answer text{i}',
        'id': i,
        'rating': random.randint(-5, 100)
    }

    for i in range(1, ANSWER_LEN + 1)
]
