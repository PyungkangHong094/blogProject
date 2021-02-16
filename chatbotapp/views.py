from django.shortcuts import render

# Create your views here.

def chathome(request):
    context = {}

    return render(request, "chatbotapp/chathome.html")