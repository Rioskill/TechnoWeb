from django.shortcuts import render
from django.core.paginator import Paginator

from mainapp.models import QUESTIONS, ANSWERS, TAGS


def get_answers(question):
    if type(question) == int:
        question_id = question
    else:
        question_id = question['id']
    return list(filter(lambda answer: answer['question_id'] == question_id, ANSWERS))


def index(request, page=1):

    p = Paginator(QUESTIONS, 7)

    questions = list()

    for question in p.page(page):
        questions.append(question)
        questions[-1]['answer_cnt'] = len(get_answers(question))

    context = {
        'questions': questions,
        'pages': list(p.page_range),
    }

    return render(request, 'index.html', context)


def tag(request, tag, page=1):
    questions = list(filter(lambda q: tag in q['tags'], QUESTIONS))

    p = Paginator(questions, 7)

    questions = list()

    for question in p.page(page):
        questions.append(question)
        questions[-1]['answer_cnt'] = len(get_answers(question))

    context = {
        'tag': tag,
        'questions': questions,
        'pages': list(p.page_range)
    }

    return render(request, 'tag.html', context)


def question(request, question_id):

    question_data = QUESTIONS[question_id - 1]

    answers_data = get_answers(question_id)

    context = {
        'question': question_data,
        'answers': answers_data,
        'answers_cnt': len(answers_data)
    }

    return render(request, 'question.html', context)


def ask(request):
    return render(request, 'ask.html', {})


def settings(request):
    return render(request, 'settings.html', {})


def login(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html', {})

