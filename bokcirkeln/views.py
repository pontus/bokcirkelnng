# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader


def mainpage(request):
    template = loader.get_template('mainpage.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))