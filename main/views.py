from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.html import escape

def index(request):
    s = ['<p>']
    if request.user.is_authenticated():
        s.append('You are signed in as <strong>%s</strong> (%s)' % (
                escape(request.user.username),
                escape(request.user.get_full_name())))
        s.append(' | <a href="/logout">Sign out</a>')
    else:
        s.append('<a href="/openid/login">Sign in with OpenID</a>')

    s.append('</p>')

    s.append('<p><a href="/private">This requires authentication</a></p>')
    return HttpResponse('\n'.join(s))
