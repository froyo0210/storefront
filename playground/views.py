from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # we use render to sent back a page work with template
    return render(request, 'hello.html', {'name': 'Momo'})