


from django.http import HttpResponse
from django.shortcuts import render

from assignments.models import About
from blog_main.forms import RegistrationForm
from blogs.models import Blog, Category
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')

    try:

        about = About.objects.get()
    except:
        
        about = None

    context = {
        
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render('register')
        else:
            print(form.errors)

    else:
        form = RegistrationForm()
    context = {
        'form' : form,
    }
    
    return render(request, 'register.html', context)


def login(request):
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


