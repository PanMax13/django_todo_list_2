from django.shortcuts import render, get_object_or_404
from .models import Tasks, Tables
# Create your views here.

def show_all_tasks(request):
    tasks = Tasks.objects.all()
    tables = Tables.objects.all()

    context = {
        'tables': tables,
        'tasks': tasks,
    }
    return render(request, 'helper.html', context)


def filter_by_slug(request, slug="all"):
    categories = Tables.objects.all()
    tasks = Tasks.objects.all()

    if slug != 'all':
        category = Tables.objects.get(slug=slug)
        category_id = category.id

        tasks = Tasks.objects.filter(category_id=category_id)

    context = {
        'categories': categories,
        'tasks': tasks,
        'slug': slug
    }

    return render(request, 'helper.html', context)