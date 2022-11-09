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

QUESTIONS = [
    {
        'title': f'Question {i}',
        'text': f'text {i}',
        'id': i,
        'tags': random.sample(TAGS, i % (len(TAGS) - 2) + 1),
        'rating': random.randint(-5, 100)
    }
    for i in range(1, 31)
]

ANSWERS = [
    {
        'question_id': random.randint(0, 30),
        'text': f'answer text{i}',
        'id': i,
        'rating': random.randint(-5, 100)
    }

    for i in range(1, 100)
]
