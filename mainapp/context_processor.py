from mainapp.models import TAGS


def sidebar_tags(request):
    return {
        'tags': [TAGS[i:i+3] for i in range(0, len(TAGS), 3)],
        # 'authorized': True
    }
