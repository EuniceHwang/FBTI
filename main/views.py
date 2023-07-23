from django.shortcuts import render
from .models import Question, Food, Choice

def index(request):
    foods = Food.objects.all()
    
    context = {
        'foods': foods,
    }
    
    return render(request, 'index.html', context=context)

def form(request):
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }
    
    return render(request, 'form.html', context)

def result(request):
    
    # 문항 수
    N = Question.objects.count()
    # 음식 유형 수
    K = Food.objects.count()
    
    # 음식 유형마다 몇 개인지 저장할 리스트 counter[1] = (1번 유형 점수(개수))
    counter = [0] * (K + 1)
    
    for n in range(1, N+1):
        food_id = int(request.POST[f'question-{n}'][0])
        counter[food_id] += 1
    print(counter)
    # 최고점 음식 유형
    best_food_id = max(range(1, K + 1), key=lambda id: counter[id])
    best_food = Food.objects.get(pk=best_food_id)
    best_food.count += 1
    best_food.save()
    
    context = {
        'food': best_food,
        'counter': counter
    }
    
    return render(request, 'result.html', context)