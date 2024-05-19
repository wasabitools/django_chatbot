from django.conf import settings
import openai
from django.http import JsonResponse
from django.shortcuts import render


client = openai.OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def question_openai(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": message}],
        stop=None,
        n=1,
        temperature=0.1
    )
    answer = response.choices[0].message.content
    return answer


def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = question_openai(message)
        return JsonResponse({"message": message, "response": response})
    return render(request, "chatbot.html")
