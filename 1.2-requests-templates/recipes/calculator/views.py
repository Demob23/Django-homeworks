from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    msg = 'Добро пожаловать!'
    return HttpResponse(msg)


def recipe_list(request):
    msg = 'На сайте есть рецепты: '
    for dish in DATA:
        msg += dish + '; '
    return HttpResponse(msg)


def check_servings(request, recipe):
    dish = {
        'recipe': {}
    }
    if request.GET.get('servings'):
        for ingredient, amount in DATA[recipe].items():
            dish['recipe'].update({ingredient: amount * int(request.GET.get('servings'))})
    return dish

def recipe_view(request, recipe):
    try:
        context = {
            'recipe': DATA[recipe]
        }

        dish = check_servings(request, recipe)
    except KeyError:
        context = {}
    template_name = 'calculator/index.html'

    return render(request, template_name, dish)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
