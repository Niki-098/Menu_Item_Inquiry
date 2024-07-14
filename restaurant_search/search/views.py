from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from search.models import Dish

def search(request):
    query = request.GET.get('q')
    if query:
        results = Dish.objects.filter(items__icontains=query).order_by('-id')
    else:
        results = Dish.objects.none()
    return render(request, 'search/results.html', {'results': results, 'query': query})

