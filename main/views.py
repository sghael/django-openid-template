from django.contrib.auth.decorators import login_required
from django.http                    import HttpResponse
from django.shortcuts               import render_to_response
from django.template                import RequestContext

def index(request):
    return render_to_response('main/index.html', {
    },context_instance=RequestContext(request))
    
@login_required
def require_authentication(request):
    return HttpResponse('This page requires authentication')
