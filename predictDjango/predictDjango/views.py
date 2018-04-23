from django.shortcuts import render
from .predictors import predict

def home(request):
    context = {}
    x = request.GET.get('input')
    if x:
        y = predict(float(x))
        context['answer'] = y
    return render(request, 'home.html', context)
