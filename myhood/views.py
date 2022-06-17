from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, 'neighborhood/index.html')

@login_required(login_url='login')
def feed(request):
    current_user = request.user.profile
    posts = models.Post.objects.filter(hood=current_user.neighborhood)

    if request.method == 'POST':
        new_post_form = NewPostForm(request.POST)
        if new_post_form.is_valid():
            new_post_form.instance.user = current_user
            new_post_form.instance.hood = current_user.neighborhood
            new_post_form.save()

            return redirect('feed')
    else:
        new_post_form = NewPostForm()

    title = 'Feed'
    context = {
        'title': title,
        'posts': posts,
        'new_post_form': new_post_form,
    }

    return render(request, 'neighborhood/feed.html',context)
