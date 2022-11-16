from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    avatar = models.ImageField()


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)


class QuestionManager(models.Manager):
    def in_rating_order(self):
        queryset = self.get_queryset().annotate(
            rating_sum=Coalesce(Sum('questionvote__vote'), 0)
        )
        return queryset.order_by('-rating_sum')

    def with_tag(self, tag_name):
        queryset = self.get_queryset()
        return queryset.filter(tags__tag_name__exact=tag_name)


class Question(models.Model):
    title = models.TextField()
    text = models.TextField()
    tags = models.ManyToManyField(to=Tag)
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    @property
    def answer_cnt(self):
        return Answer.objects.filter(question=self).count()

    @property
    def rating(self):
        return sum(QuestionVote.objects.filter(question=self).values_list('vote', flat=True))

    objects = QuestionManager()


class AnswerManager(models.Manager):
    def for_question(self, question):
        queryset = self.get_queryset()
        return queryset.filter(question=question)


class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    @property
    def rating(self):
        return sum(AnswerVote.objects.filter(answer=self).values_list('vote', flat=True))

    objects = AnswerManager()


class VoteChoice(models.IntegerChoices):
    like = 1
    dislike = -1


class QuestionVote(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VoteChoice.choices)


class AnswerVote(models.Model):
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VoteChoice.choices)
