from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'chatbot/index.html');


def ask(request):
    return render(request, 'chatbot/ask.html');