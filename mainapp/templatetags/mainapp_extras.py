from django import template

register = template.Library()


@register.filter
def add_page_number(url, page):
    return url + '/' + str(page)


@register.filter
def add_next_page_number(url, page):
    return url + '/' + str(page + 1)


@register.filter
def add_prev_page_number(url, page):
    return url + '/' + str(page - 1)
