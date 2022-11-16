from django.core.management.base import BaseCommand, CommandError
from django.core.files.images import ImageFile
from mainapp.models import *
from faker import Faker
from faker.providers.person.en import Provider as nickname_provider
import random
import os


class Command(BaseCommand):
    help = "fills database with fake data"
    fake = Faker()

    def create_fake_users(self, cnt):

        nicknames = list(set(nickname_provider.first_names))
        random.shuffle(nicknames)

        nicknames_cnt = len(nicknames)

        for i in range(nicknames_cnt, cnt):
            nicknames.append(nicknames[i % nicknames_cnt] + f"-{i // nicknames_cnt + 1}")

        users = [User(username=nicknames[i],
                      email=self.fake.email(),
                      password=self.fake.password())
                 for i in range(cnt)]

        return users

    def create_fake_questions(self, cnt):

        users = list(User.objects.all())

        questions = [Question(title=self.fake.sentence(),
                              text=self.fake.paragraph(),
                              author=random.choice(users))
                     for _ in range(cnt)]

        return questions

    def create_fake_answers(self, cnt):

        users = list(User.objects.all())
        questions = list(Question.objects.all())

        answers = [Answer(question=random.choice(questions),
                          text=self.fake.paragraph(),
                          author=random.choice(users))
                   for _ in range(cnt)]

        return answers

    @staticmethod
    def create_fake_votes(cnt):
        users = list(User.objects.all())
        questions = list(Question.objects.values_list('id', flat=True))

        question_votes = [QuestionVote(question_id=random.choice(questions),
                                       author=random.choice(users),
                                       vote=random.choice([-1, 1]))
                          for _ in range(cnt)]

        answers = list(Answer.objects.values_list('id', flat=True))

        answer_votes = [AnswerVote(answer_id=random.choice(answers),
                                   author=random.choice(users),
                                   vote=random.choice([-1, 1]))
                        for _ in range(cnt)]

        return question_votes, answer_votes

    def bulk_create_fake_tags(self, cnt):

        tags = [Tag(tag_name=name) for name in self.fake.words(nb=cnt)]

        Tag.objects.bulk_create(tags, batch_size=10000)

        tag_ids = Tag.objects.values_list('id', flat=True)

        questions = list(Question.objects.all())

        links = set((random.choice(tag_ids), random.choice(questions)) for _ in range(len(questions) * 3))

        tag_to_question_links = [Question.tags.through(tag_id=link[0],
                                                       question=link[1])
                                 for link in links]

        Question.tags.through.objects.bulk_create(tag_to_question_links, batch_size=10000)

    def add_arguments(self, parser):
        parser.add_argument('ration', type=int)

    def handle(self, *args, **options):

        cnt = options['ration']
        users = self.create_fake_users(cnt)

        print('generated users')

        User.objects.bulk_create(users, batch_size=10000)

        del users

        print('saved users')

        questions = self.create_fake_questions(cnt * 10)

        print('generated questions')

        Question.objects.bulk_create(questions, batch_size=10000)

        del questions

        print('saved questions')

        answers = self.create_fake_answers(cnt * 100)

        print('generated answers')

        Answer.objects.bulk_create(answers, batch_size=10000)

        del answers

        print('saved answers')

        questions_votes, answer_votes = self.create_fake_votes(cnt * 100)

        print('generated votes')

        QuestionVote.objects.bulk_create(questions_votes, batch_size=10000)
        AnswerVote.objects.bulk_create(answer_votes, batch_size=10000)

        del questions_votes
        del answer_votes

        print('saved votes')

        self.bulk_create_fake_tags(cnt)

        print('created tags')

