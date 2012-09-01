from django.shortcuts import render_to_response

def hello(request):
    return render_to_response('template_hello.html', {'text':'Hello, world!'})
