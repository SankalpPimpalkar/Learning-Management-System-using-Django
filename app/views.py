from django.shortcuts import render
from .models import Course
from django.db.models import Q

# Create your views here.
def home(request):
    search_query = request.GET.get('search', '').strip()
    is_approved = request.GET.get('approved') == 'true'
    date_orderAsc = request.GET.get('date_orderAsc') == 'on'
    courses = Course.objects.all()

    if search_query:
        courses = courses.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query)
        )

    if is_approved:
        courses = courses.filter(is_approved=True)

    courses = courses.order_by('published_date' if date_orderAsc == True else '-published_date')

    context = {
        'courses': courses,
        'search_query': search_query,
        'is_approved': is_approved,
        'date_order': date_orderAsc,
    }
    return render(request, 'home.html', context)