from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        'questions': [
            1, 2, 3
        ]
    }

    return render(request, 'index.html', context)


def question(request):
    return render(request, 'question.html', {})
