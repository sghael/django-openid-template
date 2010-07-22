from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.html import escape


def next_works(request):
    return HttpResponse('?next= bit works. <a href="/">Home</a>')


@login_required
def require_authentication(request):
    return HttpResponse('This page requires authentication')
