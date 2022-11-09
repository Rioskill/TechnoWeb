from django.shortcuts import render
from django.core.paginator import Paginator

from mainapp.models import QUESTIONS, ANSWERS, TAGS


def paginate(object_list, page, per_page=7):
    p = Paginator(object_list, per_page)
    return p.page(page), list(p.get_elided_page_range(page, on_each_side=2, on_ends=1))


def get_answers(question):
    if type(question) == int:
        question_id = question
    else:
        question_id = question['id']
    return list(filter(lambda answer: answer['question_id'] == question_id, ANSWERS))


def add_answers_cnt_to_questions(questions):
    res_questions = list()

    for question in questions:
        res_questions.append(question)
        res_questions[-1]['answer_cnt'] = len(get_answers(question))

    return res_questions


def index(request, page=1):
    paginated_questions, pages = paginate(QUESTIONS, page)
    questions = add_answers_cnt_to_questions(paginated_questions)

    context = {
        'list_url': '/index',
        'questions': questions,
        'pages': pages,
        'current_page': page
    }

    return render(request, 'index.html', context)


def tag(request, tag, page=1):
    questions = list(filter(lambda q: tag in q['tags'], QUESTIONS))

    paginated_questions, pages = paginate(questions, page)
    questions = add_answers_cnt_to_questions(paginated_questions)

    context = {
        'tag': tag,
        'list_url': f'/tag/{tag}',
        'questions': questions,
        'pages': pages,
        'current_page': page
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

