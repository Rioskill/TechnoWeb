from django.shortcuts import render, Http404
from django.core.paginator import Paginator

from mainapp.models import *


def paginate(object_list, page, per_page=7):
    if page < 0 or page >= len(object_list):
        page = 1

    p = Paginator(object_list, per_page)
    return p.get_page(page), list(p.get_elided_page_range(page, on_each_side=2, on_ends=1))


def index(request, page=1):
    questions, pages = paginate(list(Question.objects.all()), page)

    context = {
        'list_url': '/index',
        'questions': questions,
        'pages': pages,
        'current_page': page
    }

    return render(request, 'index.html', context)


def hot(request, page=1):
    sorted_questions = Question.objects.in_rating_order()

    paginated_questions, pages = paginate(sorted_questions, page)

    context = {
        'list_url': '/hot',
        'questions': paginated_questions,
        'pages': pages,
        'current_page': page
    }

    return render(request, 'hot.html', context)


def tag(request, tag, page=1):
    questions = Question.objects.with_tag(tag)

    paginated_questions, pages = paginate(questions, page)

    context = {
        'tag': tag,
        'list_url': f'/tag/{tag}',
        'questions': paginated_questions,
        'pages': pages,
        'current_page': page
    }

    return render(request, 'tag.html', context)


def question(request, question_id, page=1):
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.for_question(question)

    paginated_answers, pages = paginate(answers, page)

    context = {
        'question': question,
        'answers': paginated_answers,
        'answers_cnt': answers.count(),
        'pages': pages,
        'current_page': page,
        'list_url': f'/question/{question_id}'
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


def page_not_found_view(request, exception):
    return Http404()

