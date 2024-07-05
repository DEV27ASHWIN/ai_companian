from django.shortcuts import render
from django.http import JsonResponse
import ollama
import json

def format_history(msg, history, system_prompt):
    chat_history = [{"role": "system", "content": system_prompt}]
    for query, response in history:
        chat_history.append({"role": "user", "content": query})
        chat_history.append({"role": "assistant", "content": response})  
    chat_history.append({"role": "user", "content": msg})
    return chat_history

def generate_response(msg, history):
    system_prompt = "This AI is knowledgeable in physical and mental health, education sector, and Human Psychology. For any inquiries outside these areas, it will apologize and indicate its limited expertise."
    chat_history = format_history(msg, history, system_prompt)
    response = ollama.chat(model='llama2', stream=True, messages=chat_history)
    message = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        message += token
    return message

def index(request):
    return render(request, 'chat/index.html')

def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            msg = data.get('message')
            history = data.get('history', [])
            if not msg:
                return JsonResponse({'error': 'Invalid request payload'}, status=400)
            response = generate_response(msg, history)
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
