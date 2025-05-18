from django.shortcuts import render, redirect
from .models import Meal
from .forms import MealForm
from datetime import date

def index(request):
    today_meals = Meal.objects.filter(date=date.today())
    total_calories = sum(meal.calories for meal in today_meals)
    return render(request, 'tracker/index.html', {'meals': today_meals, 'total_calories': total_calories})

def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MealForm()
    return render(request, 'tracker/add_meal.html', {'form': form})
