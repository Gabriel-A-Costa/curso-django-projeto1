from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from .models import Recipe
# For search type OR
from django.db.models import Q
# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context)


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    context = {
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category',
    }
    return render(request, 'recipes/pages/category.html', context)


def recipe(request, id):
    recipe = get_object_or_404(
        Recipe.objects.filter(
            pk=id,
            is_published=True
        )
    )

    context = {
        'recipe': recipe,
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context)


def search(request):
    # strip() remove backspace
    search_term = request.GET.get('q', ' ').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ), is_published=True
    ).order_by('-id')

    context = {
        'search_term': search_term,
        'search_title': f'Search for "{search_term}"',
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/search.html', context)
