from django.http import JsonResponse
from .models import ModelProvider
from django.shortcuts import render

def models_list(request):
    models = ModelProvider.objects.all()
    model_names = [model.name for model in models]
    return JsonResponse(model_names, safe=False)

def index(request):
    return render(request, 'chat/index.html')
