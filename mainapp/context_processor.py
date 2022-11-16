from mainapp.models import Question, Tag
from django.db import connection


def sidebar_tags(request):
    with connection.cursor() as cursor:
        cursor.execute("""select tag_name
                          from ( select tag.tag_name, count(votes)
                          from mainapp_question q, mainapp_questionvote votes, mainapp_tag tag, mainapp_question_tags link
                          where votes.question_id = q.id
                            and link.tag_id = tag.id
                            and link.question_id = q.id
                          group by tag.id) vote_cnt
                          order by vote_cnt.count desc
                          limit 9""")
        tags = [tag[0] for tag in cursor.fetchall()]

    return {
        'tags': [tags[i:i+3] for i in range(0, len(tags), 3)],
        'authorized': True
    }
