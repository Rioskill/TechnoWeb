"""AskStarling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mainapp.views import index, question, tag, ask, settings, login, register, hot

urlpatterns = [
    path('', index, name='index'),
    path('index/<int:page>', index, name='index-page'),
    path('tag/<str:tag>/', tag, name='tag'),
    path('tag/<str:tag>/<int:page>', tag, name='tag-page'),
    path('hot/', hot, name='hot'),
    path('hot/<int:page>', hot, name='hot-page'),
    path('question/<int:question_id>', question, name='question'),
    path('ask', ask, name='ask'),
    path('settings', settings, name='settings'),

    path('login', login, name='login'),
    path('signup', register, name='register')
]
