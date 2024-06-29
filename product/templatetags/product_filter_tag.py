from django import template

register = template.Library()


@register.filter()
def cm_dislike_checker(cm, user):
    if cm.dislikers.filter(id=user.id).exists():
        return 'fa-solid'

    return 'fa-regular'


@register.filter()
def cm_like_checker(cm, user):
    if cm.likers.filter(id=user.id).exists():
        return 'fa-solid'
    return 'fa-regular'


@register.filter()
def pr_like_checker(rep, user):
    if rep.likers.filter(id=user.id).exists():
        return 'fa-solid'
    return 'fa-regular'


@register.filter()
def reply_like_checker(pr, user):
    if pr.likers_reply.filter(id=user.id).exists():
        return 'fa-solid'
    return 'fa-regular'
