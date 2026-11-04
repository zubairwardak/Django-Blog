from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogs.models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):
    # Fetch posts based on the category_id
    posts = Blog.objects.filter(status='Published', category = category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except :
        return redirect('home')  # Redirect to home if category not found
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)