from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sessions.models import Session

def hello_view(request):
    # Set a session variable
    request.session['user'] = 'Hello, World!'

    # Create an HttpResponse object to set a cookie
    response = HttpResponse("Hello, World! Session and Cookie are set.")
    
    # Set a cookie
    response.set_cookie('dj4e_cookie', 'a2b0b375', max_age=1000)
    
    return response

