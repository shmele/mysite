from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def hello(request):
    t = get_template('template_hello.html')
    html = t.render(Context({'text':'Hello world!'}))

    return HttpResponse(html)