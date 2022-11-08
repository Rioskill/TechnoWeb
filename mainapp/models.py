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
        'tags': random.sample(TAGS, i % (len(TAGS) - 2) + 1)
    }
    for i in range(1, 31)
]

ANSWERS = [
    {
        'text': f'answer text{i}',
        'id': i
    }

    for i in range(1, 4)
]
