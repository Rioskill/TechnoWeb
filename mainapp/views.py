from django.shortcuts import render
from django.core.paginator import Paginator

from mainapp.models import QUESTIONS, ANSWERS, TAGS


def index(request, page=1):

    p = Paginator(QUESTIONS, 7)

    context = {
        'questions': p.page(page),
        'pages': list(p.page_range),
    }

    return render(request, 'index.html', context)


def tag(request, tag):
    questions = list(filter(lambda q: tag in q['tags'], QUESTIONS))

    p = Paginator(questions, 7)

    context = {
        'questions': questions,
        'pages': list(p.page_range)
    }

    return render(request, 'index.html', context)


def question(request, question_id):

    question_data = QUESTIONS[question_id]

    context = {
        'question': question_data,
        'answers': ANSWERS,
    }

    return render(request, 'question.html', context)


def ask(request):

    return render(request, 'ask.html', {})
