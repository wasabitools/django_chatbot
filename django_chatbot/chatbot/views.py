from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = "I'm fucking talking to you."
        return JsonResponse({'message': message, 'response': response})
    return render(request, "chatbot.html")